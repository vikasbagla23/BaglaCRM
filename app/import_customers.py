
import pandas as pd
import sqlite3
import re
import os
import glob
from datetime import datetime

files = glob.glob("../tally_exports/*.xlsx")

if not files:
    print("No Excel file found in tally_exports folder.")
    exit()

EXCEL_FILE = max(files, key=os.path.getmtime)

print("Using file:", EXCEL_FILE)
DB_FILE = "../data/customers.db"

df = pd.read_excel(EXCEL_FILE, header=None)

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

count = 0

for i in range(len(df)):

    cell = str(df.iloc[i, 0])

    if cell.strip() == "Ledger:":

        ledger_text = str(df.iloc[i, 1]).strip()

        match = re.match(r"(BRC)\s*(\d+)\s*(.*)", ledger_text)

        if not match:
            continue

        customer_code = f"BRC{match.group(2)}"
        customer_name = match.group(3).strip()

        address_row = str(df.iloc[i + 1, 1])
        
        phone = ""
        phone_patterns = re.findall(r"(?:\d[\s-]?){10,}", address_row)
        for p in phone_patterns:

            cleaned = re.sub(r"\D", "", p)

            if len(cleaned) == 10:
                phone = cleaned
                break




        dob_match = re.search(
            r"(\d{2}[./-]\d{2}[./-]\d{4})",
            address_row
        )

        dob = ""
        birth_day = None
        birth_month = None

        if dob_match:

         dob = dob_match.group(1)

        # Convert all separators to "/"
        dob = dob.replace("-", "/")
        dob = dob.replace(".", "/")

        try:
            d = datetime.strptime(dob, "%d/%m/%Y")
            birth_day = d.day
            birth_month = d.month

        except:
            birth_day = None
            birth_month = None

        address = address_row

        if phone:
            address = address.replace(phone, "")

        if dob:
            address = address.replace(dob, "")

        address = address.replace("D O B", "")
        address = address.replace(",", " ")
        address = address.strip()

        cursor.execute("""
        INSERT OR REPLACE INTO customers (
            customer_code,
            customer_name,
            phone,
            dob,
            birth_day,
            birth_month,
            address,
            updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
        """,
        (
            customer_code,
            customer_name,
            phone,
            dob,
            birth_day,
            birth_month,
            address
        ))

        count += 1

conn.commit()
conn.close()

print(f"{count} customers imported successfully!")