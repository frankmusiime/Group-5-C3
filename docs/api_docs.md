# API Documentation
Base URL
http://localhost:8000

**1. GET /transactions**

Description: Retrieve all transactions.

**Request Example (curl):**

curl -u frank:Group5@1 http://localhost:8000/transactions


Response Example (200 OK):

[
    {
        "id": 1,
        "transaction_id": "12345678",
        "category": "Incoming Money",
        "sms_body": "You received 5000 RWF from Alice",
        "sms_date": "2025-09-27",
        "sms_time": "14:30:00",
        "amount": 5000.00,
        "type": "credit",
        "currency": "RWF",
        "source": "SMS",
        "created_at": "2025-09-27T14:30:05"
    },
    {
        "id": 2,
        "transaction_id": "87654321",
        "category": "Payment",
        "sms_body": "Payment to Bob 2000 RWF",
        "sms_date": "2025-09-28",
        "sms_time": "10:15:00",
        "amount": 2000.00,
        "type": "debit",
        "currency": "RWF",
        "source": "SMS",
        "created_at": "2025-09-28T10:15:10"
    }
]

**2. GET /transactions/{id}**

Description: Retrieve a single transaction by its ID.

**Request Example (curl):**

curl -u frank:Group5@1 http://localhost:8000/transactions/1


Response Example (200 OK):

{
    "id": 1,
    "transaction_id": "12345678",
    "category": "Incoming Money",
    "sms_body": "You received 5000 RWF from Alice",
    "sms_date": "2025-09-27",
    "sms_time": "14:30:00",
    "amount": 5000.00,
    "type": "credit",
    "currency": "RWF",
    "source": "SMS",
    "created_at": "2025-09-27T14:30:05"
}


Error Example (404 Not Found):

{
    "error": "Transaction not found"
}

**3. POST /transactions**

Description: Create a new transaction.

Request Body Example (JSON):

{
    "transaction_id": "99999999",
    "category": "Incoming Money",
    "sms_body": "You received 5000 RWF from Alice",
    "sms_date": "2025-09-27",
    "sms_time": "14:30:00",
    "amount": 5000,
    "type": "credit",
    "currency": "RWF",
    "source": "SMS"
}


Request Example (curl):

curl -u frank:Group5@1 -X POST http://localhost:8000/transactions \
-H "Content-Type: application/json" \
-d '{"transaction_id":"99999999","category":"Incoming Money","sms_body":"You received 5000 RWF from Alice","sms_date":"2025-09-27","sms_time":"14:30:00","amount":5000,"type":"credit","currency":"RWF","source":"SMS"}'


Response Example (201 Created):

{
    "message": "Transaction created",
    "id": 3
}


Error Example (400 Bad Request):

{
    "error": "Missing required fields"
}

**4. PUT /transactions/{id}**

Description: Update an existing transaction by ID. Only fields provided in JSON will be updated.

Request Body Example (JSON):

{
    "category": "Payment to Code Holder",
    "amount": 5500,
    "sms_body": "Updated transaction SMS body"
}


**Request Example (curl):**

curl -u frank:Group5@1 -X PUT http://localhost:8000/transactions/1 \
-H "Content-Type: application/json" \
-d '{"category":"Payment to Code Holder","amount":5500,"sms_body":"Updated transaction SMS body"}'


Response Example (200 OK):

{
    "message": "Transaction updated"
}


Error Example (404 Not Found):

{
    "error": "Transaction not found"
}


Error Example (400 Bad Request):

{
    "error": "Invalid field data"
}

**5. DELETE /transactions/{id}**

Description: Delete a transaction by ID.

**Request Example (curl):**

curl -u frank:Group5@1 -X DELETE http://localhost:8000/transactions/1


Response Example (200 OK):

{
    "message": "Transaction deleted"
}


Error Example (404 Not Found):

{
    "error": "Transaction not found"
}

Common Error Codes
Status Code	Description
200	OK / Successful operation
201	Created / Resource created
400	Bad Request / Invalid request data
401	Unauthorized / Invalid credentials
404	Not Found / Resource not found
500	Internal Server Error / Server issue

This documentation covers all endpoints, request formats, response examples, and common error codes.
