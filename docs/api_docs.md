API Documentation

Authentication
All endpoints require Basic Authentication:
- Username: admin
- Password: alu@123

Endpoints

1. Get All Transactions
Endpoint & Method: GET /transactions
Request Example:
curl -u admin:alu@123 http://localhost:8080/transactions
Response Example:
[ ...JSON array of transactions... ]
Error Codes:
401 Unauthorized – Missing or invalid credentials

2. Get Transaction by ID
Endpoint & Method: GET /transactions/{transaction_id}
Request Example:
curl -u admin:alu@123 http://localhost:8080/transactions/76662021700
Response Example:
{"transaction_id": "76662021700", "type": "1", "amount": "", "sender": "M-Money", "receiver": "", "timestamp": "10 May 2024 4:30:58 PM", "new_balance": "", "message": "You have received 2000 RWF from Jane Smith (*********013) on your mobile money account at 2024-05-10 16:30:51. Message from sender: . Your new balance:2000 RWF. Financial Transaction Id: 76662021700.", "financial_transaction_id": "76662021700", "service_center": "+250788110381", "fee": ""}
Error Codes:
401 Unauthorized – Missing or invalid credentials
404 Not Found – Transaction not found

3. Create Transaction
Endpoint & Method: POST /transactions
Request Example:
curl -u admin:alu@123 -X POST http://localhost:8080/transactions -H "Content-Type: application/json" -d '{"transaction_id": "123456789", ...}'
Response Example:
{ ...JSON transaction object... }
Error Codes:
401 Unauthorized – Missing or invalid credentials
404 Not Found – Invalid endpoint

4. Update Transaction
Endpoint & Method: PUT /transactions/{transaction_id}
Request Example:
curl -u admin:alu@123 -X PUT http://localhost:8080/transactions/123456789 -H "Content-Type: application/json" -d '{"transaction_id": "123456789", ...}'
Response Example:
{ ...JSON transaction object... }
Error Codes:
401 Unauthorized – Missing or invalid credentials
404 Not Found – Transaction not found or invalid endpoint

5. Delete Transaction
Endpoint & Method: DELETE /transactions/{transaction_id}
Request Example:
curl -u admin:alu@123 -X DELETE http://localhost:8080/transactions/123456789
Response Example:
Transaction deleted
Error Codes:
401 Unauthorized – Missing or invalid credentials
404 Not Found – Transaction not found or invalid endpoint.
