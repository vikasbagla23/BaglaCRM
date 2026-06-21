import sqlite3

# Connect database
conn = sqlite3.connect("../data/customers.db")
cursor = conn.cursor()

# Fetch logs
cursor.execute("""
SELECT sent_date,
       message_type,
       customer_code,
       status
FROM message_log
ORDER BY id DESC
""")

logs = cursor.fetchall()

print()
print("=" * 70)
print("MESSAGE HISTORY")
print("=" * 70)

if len(logs) == 0:

    print("No messages found.")

else:

    for log in logs:

        print(
            log[0],
            " | ",
            log[1],
            " | ",
            log[2],
            " | ",
            log[3]
        )

print()
print("=" * 70)

conn.close()