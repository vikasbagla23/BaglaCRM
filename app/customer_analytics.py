import sqlite3

# Connect database
conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

# Input customer code
customer_code = input("Enter Customer Code: ").upper()

# Get customer details
cursor.execute("""
SELECT customer_name,
       phone
FROM customers
WHERE customer_code = ?
""", (customer_code,))

customer = cursor.fetchone()

if customer:

    name = customer[0]
    phone = customer[1]

    print()
    print("Customer Code :", customer_code)
    print("Name          :", name)
    print("Phone         :", phone)

    # Purchase history
    cursor.execute("""
    SELECT purchase_date,
           bill_amount
    FROM purchase_history
    WHERE customer_code = ?
    """, (customer_code,))

    purchases = cursor.fetchall()

    if purchases:

        print()
        print("Purchase History")
        print("-" * 40)

        total_purchase = 0

        for purchase in purchases:

            print(purchase[0], " ₹", purchase[1])

            total_purchase += purchase[1]

        visits = len(purchases)

        average_bill = total_purchase / visits

        print("-" * 40)
        print("Total Purchase : ₹", total_purchase)
        print("Number of Visits :", visits)
        print("Average Bill : ₹", round(average_bill, 2))

    else:

        print()
        print("No purchases found.")

else:

    print()
    print("Customer not found.")

conn.close()