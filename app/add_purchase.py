import sqlite3
from datetime import datetime

# Connect database
conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

# Input
customer_code = input("Enter Customer Code: ").upper()
bill_amount = float(input("Enter Bill Amount: "))

# Current date
purchase_date = datetime.now().strftime("%d-%m-%Y")

# Check customer exists
cursor.execute("""
SELECT customer_name
FROM customers
WHERE customer_code = ?
""", (customer_code,))

customer = cursor.fetchone()

if customer:

    cursor.execute("""
    INSERT INTO purchase_history
    (
        customer_code,
        purchase_date,
        bill_amount
    )
    VALUES (?, ?, ?)
    """, (
        customer_code,
        purchase_date,
        bill_amount
    ))

    conn.commit()

    print()
    print("Purchase added successfully!")
    print("Customer:", customer[0])
    print("Amount: ₹", bill_amount)

else:

    print()
    print("Customer not found.")

conn.close()