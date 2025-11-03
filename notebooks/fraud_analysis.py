import pandas as pd

# --- Load --------------------------------------------------------------------
df = pd.read_csv("../data/transactions.csv", parse_dates=["txn_time"])

# --- High-value rule ---------------------------------------------------------
df["high_value_flag"] = df["amount"] > 2000  # > $2k

# --- Velocity rule (<2 minutes between user txns) ----------------------------
df = df.sort_values(["user_id", "txn_time"])
mins = (
    df.groupby("user_id")["txn_time"]
      .diff()
      .dt.total_seconds()
      .div(60)
)
df["minutes_since_prev"] = mins
df["velocity_flag_lt2m"] = df["minutes_since_prev"].fillna(9999) < 2

# --- Simple risk score (tweak weights as you like) ---------------------------
# High-value = 2 points, rapid velocity = 1 point
df["risk_score"] = (df["high_value_flag"].astype(int) * 2
                    + df["velocity_flag_lt2m"].astype(int))

# --- Optional: device anomaly (same device used by >1 user on same day) -----
device_users = (
    df.assign(txn_date=df["txn_time"].dt.date)
      .groupby(["txn_date","device_id"])["user_id"]
      .nunique()
      .reset_index(name="distinct_users")
)
device_risky = device_users.query("distinct_users > 1")[["txn_date","device_id"]]
df["device_anomaly"] = df.merge(
    device_risky, how="left",
    left_on=[df["txn_time"].dt.date, "device_id"],
    right_on=["txn_date","device_id"]
)["txn_date"].notna()

# --- Optional: country change within 24h (impossible-travel-ish) ------------
df["country_change_24h"] = False
for uid, g in df.sort_values("txn_time").groupby("user_id"):
    prev_country = None
    prev_time = None
    mask = []
    for _, r in g.iterrows():
        if prev_country is None:
            mask.append(False)
        else:
            hours = (r["txn_time"] - prev_time).total_seconds() / 3600
            mask.append((r["country"] != prev_country) and (abs(hours) <= 24))
        prev_country = r["country"]
        prev_time = r["txn_time"]
    df.loc[g.index, "country_change_24h"] = mask

# --- Recompute a slightly richer score if you want ---------------------------
df["risk_score_v2"] = (
    df["risk_score"]
    + df["device_anomaly"].astype(int)     # +1
    + df["country_change_24h"].astype(int) # +1
)

# --- Outputs -----------------------------------------------------------------
cols = ["user_id","amount","merchant","country","device_id","txn_time",
        "high_value_flag","velocity_flag_lt2m","device_anomaly","country_change_24h",
        "risk_score_v2"]
print("\nScored transactions:\n")
print(df[cols].sort_values(["risk_score_v2","user_id","txn_time"], ascending=[False, True, True]))

# Top risky users
top_users = (df.groupby("user_id")["risk_score_v2"].sum()
               .reset_index().sort_values("risk_score_v2", ascending=False))
print("\nUser risk totals:\n")
print(top_users)

# Save artifacts
df.to_csv("../data/transactions_scored.csv", index=False)
top_users.to_csv("../data/user_risk_totals.csv", index=False)
print("\nSaved: ../data/transactions_scored.csv and ../data/user_risk_totals.csv")
