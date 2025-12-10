try:
    age = int(input('Enter your age: '))
    income = 20
    print(f"Your age: {age}")
    risk = income / age
    print(f"Risk factor: {risk}")
except ValueError:
    print("Invalid value entered. Please enter a valid number for age.")
except ZeroDivisionError:
    print("Age cannot be 0.")

