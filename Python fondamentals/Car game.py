# Initialize an empty command string and a 'started' flag set to False.
# command is initialized as an empty string. It will store user input.
# 'started' indicates whether the car is currently running (True) or not (False).
command = ''
started = False  

# Start an infinite loop (while true) to continuously take user input and process commands.
#This loop will continue running until the user chooses to exit the program.

while True:
    # Prompt the user to enter a command, converting it to lowercase for case-insensitivity.
    command = input('>').lower()  

    # Check if the command is 'start'.
    if command == 'start':
        # If the car is already started, notify the user.
        if started:  
            print('Car is already started.')  
        else:  # If the car is not started, set 'started' to True and notify the user.
            started = True  
            print('Car started.')  

    # Check if the command is 'stop'.
    elif command == 'stop':
        # If the car is already stopped, notify the user.
        if not started:  
            print('Car is already stopped.')  
        else:  # If the car is running, set 'started' to False and notify the user.
            started = False  
            print('Car stopped.')  

    # Check if the command is 'help'.
    elif command == 'help':
        # Print a help message showing the available commands and their functions.
        print("""
start - to start the car
stop - to stop the car
quit - to quit the program
""")  

    # Check if the command is 'quit'.
    elif command == 'quit':
        # Print an exit message and break the loop, which ends the program.
        print('Exiting program.')  
        break  
    
    # If the command doesn't match any of the expected commands, notify the user that the command is unrecognized.
    else:
        print("I don't understand that command.")  
