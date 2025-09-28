#!/usr/bin/python3
"""
SMS Transactions REST API using plain Python http.server
Supports CRUD operations: GET, POST, PUT, DELETE
with Basic Authentication
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import base64
import mysql.connector

HOST = "0.0.0.0"   # Listen on all network interfaces
PORT = 8000

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "frank",
    "password": "Group5@1",
    "database": "momo_database",
    'port': 3306
}

# Define valid users for Basic Auth
USERS = {
    "admin": "adminpass",
    "frank": "Group5@1"
}


def get_db_connection():
    """Create and return a new DB connection."""
    return mysql.connector.connect(**DB_CONFIG)


def check_auth(headers):
    """Check Basic Authentication header."""
    auth_header = headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Basic "):
        return False
    try:
        encoded = auth_header.split(" ")[1]
        decoded = base64.b64decode(encoded).decode()
        username, password = decoded.split(":")
        return USERS.get(username) == password
    except Exception:
        return False


class RequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler for transactions API."""

    def _set_headers(self, code=200, content_type="application/json"):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.end_headers()

    def _auth_required(self):
        """Return True if auth fails and response sent, else False."""
        if not check_auth(self.headers):
            self.send_response(401)
            self.send_header("WWW-Authenticate",
                             'Basic realm="Transactions API"')
            self.end_headers()
            self.wfile.write(b"Authentication required")
            return True
        return False

    def _parse_id(self, path):
        """Extract ID from /transactions/{id} path."""
        parts = path.strip("/").split("/")
        if len(parts) == 2 and parts[0] == "transactions":
            return parts[1]
        return None

    # --- GET ---
    def do_GET(self):
        if self._auth_required():
            return

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            if self.path == "/transactions":
                cursor.execute(
                    "SELECT * FROM transactions "
                    "ORDER BY sms_date DESC, sms_time DESC"
                )
                transactions = cursor.fetchall()
                self._set_headers()
                self.wfile.write(json.dumps(
                    transactions, default=str).encode())
            elif self.path.startswith("/transactions/"):
                tx_id = self._parse_id(self.path)
                if not tx_id:
                    self._set_headers(400)
                    self.wfile.write(json.dumps(
                        {"error": "Invalid transaction ID"}).encode())
                    return
                cursor.execute(
                    "SELECT * FROM transactions WHERE id=%s", (tx_id,))
                transaction = cursor.fetchone()
                if transaction:
                    self._set_headers()
                    self.wfile.write(json.dumps(
                        transaction, default=str).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps(
                        {"error": "Transaction not found"}).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps(
                    {"error": "Endpoint not found"}).encode())
        except mysql.connector.Error as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode())
        finally:
            cursor.close()
            conn.close()

    # --- POST ---
    def do_POST(self):
        if self._auth_required():
            return

        if self.path != "/transactions":
            self._set_headers(404)
            self.wfile.write(json.dumps(
                {"error": "Endpoint not found"}).encode())
            return

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode())
            return

        required_fields = ["category", "sms_body",
                           "sms_date", "sms_time", "amount", "type"]
        if not all(field in data for field in required_fields):
            self._set_headers(400)
            self.wfile.write(json.dumps(
                {"error": f"Missing required fields: {required_fields}"}
            ).encode())
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO transactions (
                    transaction_id, category, sms_body,
                    sms_date, sms_time, amount, type,
                    currency, source
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                data.get("transaction_id"),
                data["category"],
                data["sms_body"],
                data["sms_date"],
                data["sms_time"],
                data["amount"],
                data["type"],
                data.get("currency", "RWF"),
                data.get("source", "SMS")
            ))
            conn.commit()
            self._set_headers(201)
            self.wfile.write(json.dumps(
                {"message": "Transaction added",
                 "id": cursor.lastrowid}).encode())
        except mysql.connector.Error as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode())
        finally:
            cursor.close()
            conn.close()

    # --- PUT ---
    def do_PUT(self):
        if self._auth_required():
            return

        if not self.path.startswith("/transactions/"):
            self._set_headers(404)
            self.wfile.write(json.dumps(
                {"error": "Endpoint not found"}).encode())
            return

        tx_id = self._parse_id(self.path)
        if not tx_id:
            self._set_headers(400)
            self.wfile.write(json.dumps(
                {"error": "Invalid transaction ID"}).encode())
            return

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode())
            return

        fields = ["transaction_id", "category", "sms_body", "sms_date",
                  "sms_time", "amount", "type", "currency", "source"]
        updates = {k: v for k, v in data.items() if k in fields}
        if not updates:
            self._set_headers(400)
            self.wfile.write(json.dumps(
                {"error": "No valid fields to update"}).encode())
            return

        set_clause = ", ".join(f"{k}=%s" for k in updates.keys())
        values = list(updates.values())
        values.append(tx_id)

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                f"UPDATE transactions SET {set_clause} WHERE id=%s", values)
            conn.commit()
            if cursor.rowcount:
                self._set_headers()
                self.wfile.write(json.dumps(
                    {"message": "Transaction updated"}).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps(
                    {"error": "Transaction not found"}).encode())
        finally:
            cursor.close()
            conn.close()

    # --- DELETE ---
    def do_DELETE(self):
        if self._auth_required():
            return

        if not self.path.startswith("/transactions/"):
            self._set_headers(404)
            self.wfile.write(json.dumps(
                {"error": "Endpoint not found"}).encode())
            return

        tx_id = self._parse_id(self.path)
        if not tx_id:
            self._set_headers(400)
            self.wfile.write(json.dumps(
                {"error": "Invalid transaction ID"}).encode())
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM transactions WHERE id=%s", (tx_id,))
            conn.commit()
            if cursor.rowcount:
                self._set_headers()
                self.wfile.write(json.dumps(
                    {"message": "Transaction deleted"}).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps(
                    {"error": "Transaction not found"}).encode())
        finally:
            cursor.close()
            conn.close()


def run(server_class=HTTPServer, handler_class=RequestHandler):
    """Run the HTTP server."""
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server at http://{HOST}:{PORT}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
