import sqlite3

conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

search = input(
    "Enter BRC Code, Customer Name or Mobile Number: "
)

cursor.execute("""
SELECT customer_code,
       customer_name,
       phone,
       birth_day,
       birth_month
FROM customers
WHERE customer_code = ?
   OR customer_name LIKE ?
   OR phone = ?
""", (
    search.upper(),
    "%" + search + "%",
    search
))

customers = cursor.fetchall()

if customers:

    print()

    for customer in customers:

        print("Customer Code :", customer[0])
        print("Name          :", customer[1])
        print("Phone         :", customer[2])
        print(
            "Birthday      :",
            f"{customer[3]:02d}-{customer[4]:02d}"
        )
        print("-" * 40)

else:

    print()
    print("Customer not found.")

conn.close()