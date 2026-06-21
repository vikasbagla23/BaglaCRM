import shutil
from datetime import datetime

# Database file

source = r"C:\Users\hp\Desktop\BaglaCRM\data\customers.db"

# Current date and time

date_string = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# Backup file path

destination = rf"C:\Users\hp\Desktop\BaglaCRM\backups\customers_{date_string}.db"

# Create backup

shutil.copy2(source, destination)

print()
print("Backup created successfully!")

print()
print("Backup saved at:")
print(destination)
