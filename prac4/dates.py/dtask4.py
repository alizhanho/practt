from datetime import datetime

date1 = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

d1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
d2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

difference = d2 - d1
print("Difference in seconds:", difference.total_seconds())