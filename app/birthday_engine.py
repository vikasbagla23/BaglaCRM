import sqlite3
from datetime import datetime, timedelta

today = datetime(2026,11,20)

conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

cursor.execute("""
SELECT customer_code,
       customer_name,
       phone,
       birth_day,
       birth_month
FROM customers
""")

customers = cursor.fetchall()

print(f"\nToday's Date: {today.strftime('%d-%m-%Y')}")
print("-" * 60)

for customer in customers:

    code = customer[0]
    name = customer[1]
    phone = customer[2]
    birth_day = customer[3]
    birth_month = customer[4]

    birthday = datetime(today.year, birth_month, birth_day)

    pre_birthday = birthday - timedelta(days=3)
    final_reminder = birthday + timedelta(days=3)

    if today.date() == pre_birthday.date():

        print(f"PRE-BIRTHDAY REMINDER")
        print(f"{name} ({code})")
        print(f"Phone: {phone}")
        print()

    elif today.date() == birthday.date():

        print(f"BIRTHDAY WISH")
        print(f"{name} ({code})")
        print(f"Phone: {phone}")
        print()

    elif today.date() == final_reminder.date():

        print(f"FINAL REMINDER")
        print(f"{name} ({code})")
        print(f"Phone: {phone}")
        print()

conn.close()