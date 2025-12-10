from datetime import datetime

# Get current date and time
now = datetime.now()
print("Current Date and Time:", now)

# Formatting date
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_time)
