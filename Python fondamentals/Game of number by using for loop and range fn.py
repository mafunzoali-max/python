secret_number = 7
attempt_limit = 4
for i in range(attempt_limit):  # Limit the number of attempts
    attempt = int(input('Attempt: '))  # Ask for the user's guess each time
    if attempt == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed!')



