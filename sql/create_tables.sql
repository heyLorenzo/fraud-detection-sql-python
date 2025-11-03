DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
  transaction_id INTEGER,
  user_id INTEGER,
  amount FLOAT,
  merchant TEXT,
  country TEXT,
  device_id TEXT,
  txn_time DATETIME,
  status TEXT
);

INSERT INTO transactions VALUES
(1, 101,  50, 'Walmart',       'USA',    'deviceA', '2025-01-01 08:00:00', 'approved'),
(2, 101, 4500, 'BestBuy',      'USA',    'deviceA', '2025-01-01 08:01:00', 'approved'),
(3, 102,  20, 'McDonalds',     'USA',    'deviceB', '2025-01-01 09:00:00', 'approved'),
(4, 102, 3000, 'Louis Vuitton','France', 'deviceB', '2025-01-01 12:00:00', 'approved'),
(5, 103, 500, 'Apple Store',   'USA',    'deviceC', '2025-01-01 10:00:00', 'declined');
