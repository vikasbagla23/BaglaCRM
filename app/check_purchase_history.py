import sqlite3

conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

cursor.execute("""
SELECT customer_code,
       bill_amount
FROM purchase_history
""")

rows = cursor.fetchall()

print()

for row in rows:
    print(row)

print()
print("Total rows =", len(rows))

conn.close()