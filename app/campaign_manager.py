import sqlite3
import pywhatkit

# YOUR NUMBER FOR TESTING
test_number = "+918306821033"

conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

print()
print("1. Send to All Customers")
print("2. Send to VIP Customers")
print()

choice = input("Enter your choice: ")

# ==================================
# ALL CUSTOMERS
# ==================================
if choice == "1":

    cursor.execute("""
    SELECT customer_name,
           phone
    FROM customers
    """)

# ==================================
# VIP CUSTOMERS
# ==================================
elif choice == "2":

    cursor.execute("""
    SELECT customers.customer_name,
           customers.phone
    FROM customers
    JOIN purchase_history
    ON customers.customer_code = purchase_history.customer_code
    GROUP BY customers.customer_code
    HAVING SUM(purchase_history.bill_amount) >= 50000
    """)

else:

    print("Invalid choice.")
    conn.close()
    exit()

customers = cursor.fetchall()

message = """
🎉 BAGLA READYMADE CENTRE

Special Offer!

Visit us and enjoy exciting discounts on your favourite products.

We look forward to serving you.
"""

for customer in customers:

    name = customer[0]
    phone = customer[1]

    print("Sending to", name)

    pywhatkit.sendwhatmsg_instantly(
        test_number,
        message,
        wait_time=20,
        tab_close=True
    )

print()
print("Campaign completed successfully!")

conn.close()