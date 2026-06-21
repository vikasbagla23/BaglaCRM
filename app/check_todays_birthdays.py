import sqlite3
from datetime import datetime

today = datetime.now()

conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

cursor.execute("""
SELECT customer_name, phone
FROM customers
WHERE birth_day=? AND birth_month=?
""", (today.day, today.month))

rows = cursor.fetchall()

print()

for row in rows:
    print(row)

print()
print("Total birthdays =", len(rows))

conn.close()