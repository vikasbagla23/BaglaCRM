import sqlite3

# Connect database
conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

# Get total purchases customer-wise
cursor.execute("""
SELECT customers.customer_code,
       customers.customer_name,
       customers.phone,
       SUM(purchase_history.bill_amount)
FROM customers
JOIN purchase_history
ON customers.customer_code = purchase_history.customer_code
GROUP BY customers.customer_code
ORDER BY SUM(purchase_history.bill_amount) DESC
""")

customers = cursor.fetchall()

print()
print("TOP VIP CUSTOMERS")
print("-" * 60)

rank = 1

for customer in customers:

    code = customer[0]
    name = customer[1]
    phone = customer[2]
    total_purchase = customer[3]

    print(rank)
    print("Customer Code :", code)
    print("Name          :", name)
    print("Phone         :", phone)
    print("Total Purchase: ₹", round(total_purchase, 2))
    print("-" * 60)

    rank += 1

conn.close()