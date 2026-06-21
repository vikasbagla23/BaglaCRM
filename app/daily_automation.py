import os

print()
print("Starting Daily Automation...")
print()

# Birthday messages
os.system("python automatic_birthday_sender.py")

# Festival messages
os.system("python festival_messages.py")

# Database backup
os.system("python backup_database.py")

print()
print("Daily Automation Completed Successfully!")