-- Use the database
CREATE DATABASE IF NOT EXISTS momo_database;
USE momo_database;

-- Drop tables if they exist
DROP TABLE IF EXISTS system_log;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Transaction_categories;

-- Customer table
CREATE TABLE Customer (
  customerId INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  phone_number VARCHAR(15),
  status ENUM('active', 'suspended', 'close') DEFAULT 'close',
  balance DECIMAL(10,2) DEFAULT 0.02
);

-- Transaction categories table
CREATE TABLE Transaction_categories (
  Category_id INT PRIMARY KEY AUTO_INCREMENT,
  Category_name VARCHAR(50),
  Description VARCHAR(100)
);

-- Transactions table
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id VARCHAR(50) NULL,
    category VARCHAR(255) NOT NULL,
    sms_body TEXT NOT NULL,
    sms_date DATE NOT NULL,
    sms_time TIME NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    type ENUM('credit','debit') NOT NULL,
    currency VARCHAR(10) DEFAULT 'RWF',
    source VARCHAR(50) DEFAULT 'SMS',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(transaction_id, sms_date, sms_time)
);

-- System log table referencing transactions
CREATE TABLE system_log (
  log_id INT PRIMARY KEY AUTO_INCREMENT,
  transaction_id INT,
  log_message VARCHAR(100),
  log_timestamp DATETIME,
  severity VARCHAR(100),
  FOREIGN KEY (transaction_id) REFERENCES transactions(id)
);
