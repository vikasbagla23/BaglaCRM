import sqlite3

conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS purchase_history
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_code TEXT,
    purchase_date TEXT,
    bill_amount REAL
)
""")

conn.commit()

print("Purchase history table created successfully!")

conn.close()