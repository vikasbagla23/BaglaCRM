import sqlite3
from datetime import datetime, timedelta

# Connect database
conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

# Date 90 days ago
cutoff_date = datetime.now() - timedelta(days=90)

# Get latest purchase date of each customer
cursor.execute("""
SELECT customers.customer_code,
       customers.customer_name,
       customers.phone,
       MAX(purchase_history.purchase_date)
FROM customers
LEFT JOIN purchase_history
ON customers.customer_code = purchase_history.customer_code
GROUP BY customers.customer_code
""")

customers = cursor.fetchall()

print()
print("INACTIVE CUSTOMERS")
print("-" * 60)

for customer in customers:

    code = customer[0]
    name = customer[1]
    phone = customer[2]
    last_purchase = customer[3]

    if last_purchase is None:

        print()
        print("Customer Code :", code)
        print("Name          :", name)
        print("Phone         :", phone)
        print("Last Purchase : Never")
        print("-" * 60)

    else:

        purchase_date = datetime.strptime(
            last_purchase,
            "%d-%m-%Y"
        )

        if purchase_date < cutoff_date:

            print()
            print("Customer Code :", code)
            print("Name          :", name)
            print("Phone         :", phone)
            print("Last Purchase :", last_purchase)
            print("-" * 60)

conn.close()