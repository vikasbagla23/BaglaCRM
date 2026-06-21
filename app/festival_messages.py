import sqlite3
import pywhatkit
from datetime import datetime

from festival_dates import FESTIVALS
from festival_templates import festival_messages


# Current date
today = datetime.now().strftime("%d-%m")

# Connect database
conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

# Fetch customers
cursor.execute("""
SELECT customer_code,
       customer_name,
       phone
FROM customers
""")

customers = cursor.fetchall()

# Check if today is a festival
festival_name = None

for name, date in FESTIVALS.items():

    if date == today:
        festival_name = name
        break


# If today is a festival
if festival_name:

    print("Today's Festival:", festival_name)

    for customer in customers:

        code = customer[0]
        customer_name = customer[1]
        phone = customer[2]

        message = festival_messages[festival_name].format(
            name=customer_name
        )

        message_type = "FESTIVAL_" + festival_name.upper()

        cursor.execute("""
        SELECT *
        FROM message_log
        WHERE customer_code = ?
        AND message_type = ?
        AND sent_date = ?
        """, (
            code,
            message_type,
            datetime.now().strftime("%d-%m-%Y")
        ))

        existing_message = cursor.fetchone()

        if existing_message:

            print("Already sent to", customer_name)

        else:

            customer_number = "+91" + phone

            pywhatkit.sendwhatmsg_instantly(
                customer_number,
                message,
                wait_time=20,
                tab_close=True
            )

            cursor.execute("""
            INSERT INTO message_log
            (
                customer_code,
                message_type,
                sent_date,
                status
            )
            VALUES (?, ?, ?, ?)
            """, (
                code,
                message_type,
                datetime.now().strftime("%d-%m-%Y"),
                "SUCCESS"
            ))

            conn.commit()

            print("Festival message sent to", customer_name)

else:

    print("No festival today.")

conn.close()