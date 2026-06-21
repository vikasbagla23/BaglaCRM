import tkinter as tk
import sqlite3
import os

# ==========================
# DATABASE
# ==========================
conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

# Total customers
cursor.execute("SELECT COUNT(*) FROM customers")
total_customers = cursor.fetchone()[0]

# Total sales
cursor.execute("""
SELECT COALESCE(SUM(bill_amount),0)
FROM purchase_history
""")
total_sales = cursor.fetchone()[0]

# Total messages
cursor.execute("""
SELECT COUNT(*)
FROM message_log
""")
total_messages = cursor.fetchone()[0]

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

if top_customer:
    top_customer_name = top_customer[0]
else:
    top_customer_name = "None"

conn.close()

# ==========================
# FUNCTIONS
# ==========================
def import_customers():
    os.system("python import_customers.py")

def search_customer():
    os.system("python search_customer.py")

def birthday_messages():
    os.system("python automatic_birthday_sender.py")

def festival_messages():
    os.system("python festival_messages.py")

def export_excel():
    os.system("python export_customers.py")

def backup_database():
    os.system("python backup_database.py")
def add_purchase():
    os.system("python add_purchase.py")

def customer_analytics():
    os.system("python customer_analytics.py")

def vip_customers():
    os.system("python vip_customers.py")

def sales_dashboard():
    os.system("python sales_dashboard.py")

def inactive_customers():
    os.system("python inactive_customers.py")

def message_history():
    os.system("python view_message_log.py")

def campaign_manager():
    os.system("python campaign_manager.py")

def win_back_campaign():
    os.system("python win_back_campaign.py")

# ==========================
# WINDOW
# ==========================
root = tk.Tk()

root.title("BAGLA READYMADE CENTRE CRM")
root.geometry("650x700")
root.configure(bg="white")

# ==========================
# HEADING
# ==========================
heading = tk.Label(
    root,
    text="BAGLA READYMADE CENTRE CRM",
    font=("Arial", 20, "bold"),
    bg="white"
)

heading.pack(pady=20)

# ==========================
# DASHBOARD
# ==========================
tk.Label(
    root,
    text=f"Total Customers : {total_customers}",
    font=("Arial", 14),
    bg="white"
).pack()

tk.Label(
    root,
    text=f"Total Sales : ₹ {round(total_sales,2)}",
    font=("Arial", 14),
    bg="white"
).pack()

tk.Label(
    root,
    text=f"Total Messages Sent : {total_messages}",
    font=("Arial", 14),
    bg="white"
).pack()

tk.Label(
    root,
    text=f"Top Customer : {top_customer_name}",
    font=("Arial", 14),
    bg="white"
).pack()

# ==========================
# BUTTONS
# ==========================
tk.Button(
    root,
    text="Import Customers",
    width=30,
    height=2,
    bg="lightblue",
    command=import_customers
).pack(pady=10)

tk.Button(
    root,
    text="Search Customer",
    width=30,
    height=2,
    bg="lightgreen",
    command=search_customer
).pack(pady=10)

tk.Button(
    root,
    text="Birthday Messages",
    width=30,
    height=2,
    bg="orange",
    command=birthday_messages
).pack(pady=10)

tk.Button(
    root,
    text="Festival Messages",
    width=30,
    height=2,
    bg="yellow",
    command=festival_messages
).pack(pady=10)

tk.Button(
    root,
    text="Export Excel",
    width=30,
    height=2,
    bg="pink",
    command=export_excel
).pack(pady=10)

tk.Button(
    root,
    text="Backup Database",
    width=30,
    height=2,
    bg="cyan",
    command=backup_database
).pack(pady=10)
tk.Button(
    root,
    text="Add Purchase",
    width=30,
    height=2,
    command=add_purchase
).pack(pady=5)

tk.Button(
    root,
    text="Customer Analytics",
    width=30,
    height=2,
    command=customer_analytics
).pack(pady=5)

tk.Button(
    root,
    text="VIP Customers",
    width=30,
    height=2,
    command=vip_customers
).pack(pady=5)

tk.Button(
    root,
    text="Sales Dashboard",
    width=30,
    height=2,
    command=sales_dashboard
).pack(pady=5)

tk.Button(
    root,
    text="Inactive Customers",
    width=30,
    height=2,
    command=inactive_customers
).pack(pady=5)

tk.Button(
    root,
    text="Message History",
    width=30,
    height=2,
    command=message_history
).pack(pady=5)

tk.Button(
    root,
    text="Campaign Manager",
    width=30,
    height=2,
    command=campaign_manager
).pack(pady=5)

tk.Button(
    root,
    text="Win Back Campaign",
    width=30,
    height=2,
    command=win_back_campaign
).pack(pady=5)

root.mainloop()