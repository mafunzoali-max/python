
# Input birth year, month, and day
birth_year = int(input('Enter your birth year: '))
birth_month = int(input('Enter your birth month: '))
birth_day = int(input('Enter your birth day: '))

# Today's date: 10/10/2024
today_year = 2024
today_month = 10
today_day = 10

# Calculate years, months, and days
years = today_year - birth_year
months = today_month - birth_month
days = today_day - birth_day

# Adjust if current day or month is less than the birth date
if days < 0:
    months -= 1
    days += 30  # Approximate month length

if months < 0:
    years -= 1
    months += 12

# Print the result
print(f'Your age is: {years} years, {months} months, and {days} days.')
