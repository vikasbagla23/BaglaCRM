import sqlite3
from openpyxl import Workbook

# Connect database
conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

# Get customers
cursor.execute("""
SELECT customer_code,
       customer_name,
       phone,
       birth_day,
       birth_month
FROM customers
ORDER BY customer_code
""")

customers = cursor.fetchall()

# Create workbook
wb = Workbook()

# Select sheet
ws = wb.active
ws.title = "Customers"

# Headers
ws.append([
    "BRC Code",
    "Customer Name",
    "Phone Number",
    "Birth Day",
    "Birth Month"
])

# Add customer data
for customer in customers:

    ws.append([
        customer[0],
        customer[1],
        customer[2],
        customer[3],
        customer[4]
    ])

# Save Excel file
wb.save("../customers_report.xlsx")

print()
print("customers_report.xlsx created successfully!")

# Close database
conn.close()