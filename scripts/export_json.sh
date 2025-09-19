{
  "customers": [
    {
      "customerId": 1,
      "first_name": "Alice",
      "last_name": "Nkurunziza",
      "phone_number": "+250785000000",
      "status": "close",
      "balance": 0.02
    },
    {
      "customerId": 2,
      "first_name": "John",
      "last_name": "Kamau",
      "phone_number": "+254711111111",
      "status": "active",
      "balance": 1500.50
    }
  ],
  "transaction_categories": [
    {
      "Category_id": 1,
      "Category_name": "Transfer",
      "Description": "Money sent from one customer to another"
    },
    {
      "Category_id": 2,
      "Category_name": "Deposit",
      "Description": "Customer adds funds into their account"
    }
  ],
  "transactions": [
    {
      "Transaction_id": 1001,
      "Amount": 200.00,
      "Sender_id": 2,
      "Receiver_id": 1,
      "Timestamp": "2025-09-18T12:30:00",
      "Currency": "KES",
      "Status": "active",
      "Category_id": 1
    },
    {
      "Transaction_id": 1002,
      "Amount": 500.00,
      "Sender_id": 1,
      "Receiver_id": 2,
      "Timestamp": "2025-09-18T14:45:00",
      "Currency": "RWF",
      "Status": "suspended",
      "Category_id": 2
    }
  ],
  "system_logs": [
    {
      "log_id": 1,
      "Transaction_id": 1001,
      "log_message": "Transaction processed successfully",
      "log_timestamp": "2025-09-18T12:31:00",
      "Severity": "INFO"
    },
    {
      "log_id": 2,
      "Transaction_id": 1002,
      "log_message": "Transaction flagged for review",
      "log_timestamp": "2025-09-18T14:46:00",
      "Severity": "WARNING"
    }
  ]
}
