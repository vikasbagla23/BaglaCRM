import sqlite3
import pywhatkit
from datetime import datetime, timedelta

# Connect database
conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

# 90 days ago
cutoff_date = datetime.now() - timedelta(days=90)

# Get latest purchase of each customer
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

for customer in customers:

    code = customer[0]
    name = customer[1]
    phone = customer[2]
    last_purchase = customer[3]

    send_message = False

    if last_purchase is None:

        send_message = True

    else:

        purchase_date = datetime.strptime(
            last_purchase,
            "%d-%m-%Y"
        )

        if purchase_date < cutoff_date:

            send_message = True

    if send_message:

        message = f"""
🎁 Dear {name},

We miss serving you at BAGLA READYMADE CENTRE.

Visit us this week and enjoy an EXTRA 5% DISCOUNT.

We look forward to welcoming you again.
"""

        customer_number = "+91" + phone

        pywhatkit.sendwhatmsg_instantly(
            customer_number,
            message,
            wait_time=20,
            tab_close=True
        )

        print("Win-back message sent to", name)

conn.close()