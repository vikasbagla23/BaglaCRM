import sqlite3

conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM customers")
count = cursor.fetchone()[0]

print("Total Customers:", count)

cursor.execute("""
SELECT customer_code,
       customer_name,
       phone,
       dob
FROM customers
LIMIT 10
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()