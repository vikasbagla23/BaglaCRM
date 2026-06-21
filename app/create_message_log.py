import sqlite3

conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS message_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_code TEXT,
    message_type TEXT,
    sent_date TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("message_log table created successfully!")