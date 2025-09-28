import mysql.connector

DB_CONFIG = {
    "host": "0.0.0.0",
    "user": "frank",
    "password": "Group5@1"
}

# Connect to MySQL
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Read the SQL file
with open(r"C:\Users\frank\Searches\Group-5-C3\database\database_setup.sql",
          "r") as f:
    sql_commands = f.read()

# Execute each command separately
for command in sql_commands.split(";"):
    if command.strip():
        cursor.execute(command)

conn.commit()
cursor.close()
conn.close()

print("Database and tables created successfully!")
