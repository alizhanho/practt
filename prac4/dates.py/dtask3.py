from datetime import datetime

now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print("Current datetime:", now)
print("Without microseconds:", without_microseconds)