import sqlite3

# Connect database
conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

# Total customers
cursor.execute("""
SELECT COUNT(*)
FROM customers
""")

total_customers = cursor.fetchone()[0]

# Total sales
cursor.execute("""
SELECT COALESCE(SUM(bill_amount),0)
FROM purchase_history
""")

total_sales = cursor.fetchone()[0]

# Total visits
cursor.execute("""
SELECT COUNT(*)
FROM purchase_history
""")

total_visits = cursor.fetchone()[0]

# Average bill
if total_visits > 0:
    average_bill = total_sales / total_visits
else:
    average_bill = 0

# Top customer
cursor.execute("""
SELECT customers.customer_name,
       COALESCE(SUM(purchase_history.bill_amount),0)
FROM customers
LEFT JOIN purchase_history
ON customers.customer_code = purchase_history.customer_code
GROUP BY customers.customer_code
ORDER BY SUM(purchase_history.bill_amount) DESC
LIMIT 1
""")

top_customer = cursor.fetchone()

print()
print("==============================")
print("BAGLA READYMADE CENTRE")
print("SALES DASHBOARD")
print("==============================")
print()

print("Total Customers    :", total_customers)
print("Total Sales        : ₹", round(total_sales, 2))
print("Total Visits       :", total_visits)
print("Average Bill Value : ₹", round(average_bill, 2))

if top_customer:
    print("Top Customer       :", top_customer[0])

print()
print("==============================")

conn.close()