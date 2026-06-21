import pyautogui
import time
import sqlite3
import pywhatkit
from datetime import datetime, timedelta

# ==========================
# TEST DATE
# ==========================
today = datetime.now()


# ==========================
# DATABASE CONNECTION
# ==========================
conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

# ==========================
# FETCH CUSTOMERS
# ==========================
cursor.execute("""
SELECT customer_code,
       customer_name,
       phone,
       birth_day,
       birth_month
FROM customers
""")

customers = cursor.fetchall()

# ==========================
# PROCESS EACH CUSTOMER
# ==========================
for customer in customers:

    code = customer[0]
    name = customer[1]
    phone = customer[2]
    birth_day = customer[3]
    birth_month = customer[4]

    
    if birth_day is None or birth_month is None:
        continue
    birthday = datetime(today.year, birth_month, birth_day)

    pre_birthday = birthday - timedelta(days=3)
    final_reminder = birthday + timedelta(days=3)

    start_date = pre_birthday.strftime("%d-%m-%Y")
    end_date = final_reminder.strftime("%d-%m-%Y")

    # =====================================================
    # PRE-BIRTHDAY REMINDER
    # =====================================================
    if today.date() == pre_birthday.date():

        message = f"""
🎁 प्रिय {name} जी,

आपका जन्मदिन आने वाला है।

BAGLA READYMADE CENTRE की ओर से आपको Birthday Week Special Offer के तहत सभी खरीदारी पर अतिरिक्त 5% छूट प्रदान की जा रही है।

यह ऑफर {start_date} से {end_date} तक मान्य रहेगा।

हम आपका स्वागत करने के लिए उत्सुक हैं।

--------------------------------

🎁 Dear {name},

Your birthday is approaching.

As part of the Birthday Week Special Offer from BAGLA READYMADE CENTRE, you are eligible for an EXTRA 5% DISCOUNT on all purchases.

This offer is valid from {start_date} to {end_date}.

We look forward to serving you.
"""

        message_type = "PRE_BIRTHDAY"

        cursor.execute("""
        SELECT *
        FROM message_log
        WHERE customer_code = ?
        AND message_type = ?
        AND sent_date = ?
        """, (
            code,
            message_type,
            today.strftime("%d-%m-%Y")
        ))

        existing_message = cursor.fetchone()

        if existing_message:

            print("Already sent pre-birthday message to", name)

        else:

            customer_number = "+91" + phone
            print("Sending to:", customer_number)
            pywhatkit.sendwhatmsg_instantly(
                customer_number,
                message,
                wait_time=40,
                tab_close=True
            )
            time.sleep(5)

            pyautogui.press("enter")

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
                today.strftime("%d-%m-%Y"),
                "SUCCESS"
            ))

            conn.commit()

            print("Pre-birthday message sent to", name)

    # =====================================================
    # BIRTHDAY WISH
    # =====================================================
    elif today.date() == birthday.date():

        message = f"""
🎂 प्रिय {name} जी,

जन्मदिन की हार्दिक शुभकामनाएँ!

BAGLA READYMADE CENTRE की ओर से आपको सुख, समृद्धि एवं खुशियों से भरे जीवन की शुभकामनाएँ।

आपके Birthday Week Special Offer के अंतर्गत अतिरिक्त 5% छूट का लाभ अभी भी उपलब्ध है।

हम आपके स्वागत के लिए उत्सुक हैं।

--------------------------------

🎂 Dear {name},

Happy Birthday!

Everyone at BAGLA READYMADE CENTRE wishes you happiness, prosperity and a wonderful year ahead.

Your Birthday Week Special Offer with an EXTRA 5% DISCOUNT is still available.

We look forward to serving you.
"""

        message_type = "BIRTHDAY"

        cursor.execute("""
        SELECT *
        FROM message_log
        WHERE customer_code = ?
        AND message_type = ?
        AND sent_date = ?
        """, (
            code,
            message_type,
            today.strftime("%d-%m-%Y")
        ))

        existing_message = cursor.fetchone()

        if existing_message:

            print("Already sent birthday wish to", name)

        else:

            customer_number = "+91" + phone
            print("Sending to:", customer_number)
            pywhatkit.sendwhatmsg_instantly(
                customer_number,
                message,
                wait_time=40,
                tab_close=True
            )
            time.sleep(5)

            pyautogui.press("enter")

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
                today.strftime("%d-%m-%Y"),
                "SUCCESS"
            ))

            conn.commit()

            print("Birthday wish sent to", name)

    # =====================================================
    # FINAL REMINDER
    # =====================================================
    elif today.date() == final_reminder.date():

        message = f"""
⏳ प्रिय {name} जी,

आपका Birthday Week Offer आज समाप्त हो रहा है।

BAGLA READYMADE CENTRE पर खरीदारी करके अतिरिक्त 5% छूट का लाभ उठाने का यह अंतिम अवसर है।

हम आपके स्वागत के लिए उत्सुक हैं।

--------------------------------

⏳ Dear {name},

Your Birthday Week Offer ends today.

This is your final opportunity to enjoy the EXTRA 5% DISCOUNT at BAGLA READYMADE CENTRE.

We look forward to serving you.
"""

        message_type = "FINAL_REMINDER"

        cursor.execute("""
        SELECT *
        FROM message_log
        WHERE customer_code = ?
        AND message_type = ?
        AND sent_date = ?
        """, (
            code,
            message_type,
            today.strftime("%d-%m-%Y")
        ))

        existing_message = cursor.fetchone()

        if existing_message:

            print("Already sent final reminder to", name)

        else:

            customer_number = "+91" + phone
            print("Sending to:", customer_number)
            pywhatkit.sendwhatmsg_instantly(
                customer_number,
                message,
                wait_time=40,
                tab_close=True
            )
            time.sleep(5)

            pyautogui.press("enter")

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
                today.strftime("%d-%m-%Y"),
                "SUCCESS"
            ))

            conn.commit()

            print("Final reminder sent to", name)

# ==========================
# CLOSE DATABASE
# ==========================
conn.close()