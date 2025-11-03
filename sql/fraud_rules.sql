-- HIGH-VALUE FLAG
SELECT
  user_id,
  amount,
  merchant,
  country,
  device_id,
  txn_time,
  CASE
    WHEN amount > 2000 THEN 'High Risk - High Value'
    ELSE 'Normal'
  END AS risk_flag
FROM transactions;

-- VELOCITY (simple count by user)
SELECT
  user_id,
  COUNT(*) AS transaction_count
FROM transactions
GROUP BY user_id;

-- VELOCITY (within 2 minutes)
SELECT
  t1.user_id,
  t1.transaction_id AS txn_id_1,
  t1.amount AS amount_1,
  t1.txn_time AS time_1,
  t2.transaction_id AS txn_id_2,
  t2.amount AS amount_2,
  t2.txn_time AS time_2,
  TIMESTAMPDIFF(MINUTE, t1.txn_time, t2.txn_time) AS minutes_between,
  'High Risk - Velocity (<2m)' AS risk_flag
FROM transactions t1
JOIN transactions t2
  ON t1.user_id = t2.user_id
 AND t1.transaction_id < t2.transaction_id
WHERE TIMESTAMPDIFF(MINUTE, t1.txn_time, t2.txn_time) < 2;
