# 💳 Bank Card Fraud Detection Engine — SQL + Rule-Based Risk Scoring

A hands-on financial crime analysis project simulating how banks monitor card transactions in real time.

## 🎯 Objective
Apply rule-based fraud detection techniques to identify suspicious card activity using SQL logic, pattern recognition, and temporal analysis.

## 🛠️ Tech Stack
| Area | Tools |
|---|---|
Database | MySQL / SQLite  
Analysis | SQL (CASE, JOIN, GROUP BY, TIMESTAMP rules)  
Notebook (coming) | Python + Pandas  
Future UI | Streamlit dashboard  

---

## 📂 Dataset Schema

| Column | Description |
|---|---|
transaction_id | unique transaction number  
user_id | customer ID  
amount | transaction amount  
merchant | merchant name  
country | transaction country  
device_id | device fingerprint  
txn_time | timestamp  
status | approved / declined  

---

## Fraud Rules Implemented

### High-Value Risk Rule
Flags transactions > $2,000 as potential fraud.

### Velocity Check (Card Testing)
Identifies multiple rapid transactions by same user.

###  Next Rules Coming
- Time-difference anomaly (within 2 minutes)
- Device mismatch (same device, multiple users)
- Impossible travel (geo anomaly)
- Python replication + dashboard

---

##  Output Samples

### Raw Transactions
*(example screenshot)*

### High-Value Fraud Flags
*(example screenshot)*

### Velocity Pattern (Transactions per User)
*(example screenshot)*

> Screenshots will be added as `/screenshots/*.png`

---

## How to Run
Run provided `.sql` scripts in DB-Fiddle, SQLite, or MySQL.

Python notebook (coming soon) will replicate logic in pandas.

---

## Resume Bullet
**Bank Card Fraud Detection Engine — SQL, Python (in progress)**  
Designed and executed fraud-detection rules on synthetic card data, identifying high-value and velocity-based anomalies. Leveraged SQL CASE logic, aggregation, and timestamp analysis to flag suspicious activity and simulate bank fraud workflows.

---

## Open to Collaboration
Interested in fintech, fraud detection, AML, and risk analytics.  
Let’s connect & build! 
