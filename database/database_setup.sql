CREATE TABLE Customer (
  customerId INT PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  phone_number VARCHAR(15),
  status ENUM('active', 'suspended', 'close') DEFAULT 'close',
  balance DECIMAL(10,2) DEFAULT 0.02
);

CREATE TABLE Transaction_categories (
  Category_id INT PRIMARY KEY,
  Category_name VARCHAR(50),
  Description VARCHAR(100)
);

CREATE TABLE Transaction (
  Transaction_id INT PRIMARY KEY,
  Amount DECIMAL(10,2),
  Sender_id INT,
  Receiver_id INT,
  Timestamp DATETIME,
  Currency VARCHAR(25),
  Status ENUM('active', 'suspended', 'close') DEFAULT 'close',
  Category_id INT,
  FOREIGN KEY (Sender_id) REFERENCES Customer(customerId),
  FOREIGN KEY (Receiver_id) REFERENCES Customer(customerId),
  FOREIGN KEY (Category_id) REFERENCES Transaction_categories(Category_id)
);

CREATE TABLE system_log (
  log_id INT PRIMARY KEY,
  Transaction_id INT,
  log_message VARCHAR(100),
  log_timestamp DATETIME,
  Severity VARCHAR(100),
  FOREIGN KEY (Transaction_id) REFERENCES Transaction(Transaction_id)
);
