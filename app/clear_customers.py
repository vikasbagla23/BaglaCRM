import sqlite3

conn = sqlite3.connect("../data/customers.db")
cur = conn.cursor()

cur.execute("DELETE FROM customers")

conn.commit()
conn.close()

print("Customers cleared successfully!")