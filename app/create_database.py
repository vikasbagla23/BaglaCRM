import sqlite3

conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_code TEXT PRIMARY KEY,
    customer_name TEXT,
    phone TEXT,
    dob TEXT,
    birth_day INTEGER,
    birth_month INTEGER,
    address TEXT,
    premium INTEGER DEFAULT 1,
    active INTEGER DEFAULT 1,
    birthday_offer_used INTEGER DEFAULT 0,
    created_at TEXT,
    updated_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS message_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_code TEXT,
    message_type TEXT,
    sent_date TEXT,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS festival_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_code TEXT,
    festival_name TEXT,
    sent_date TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")