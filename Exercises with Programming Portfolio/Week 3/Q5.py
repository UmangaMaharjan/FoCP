''' Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time. '''

def set_password():
    # Condition to keep on asking the password
    while True: 
        password1 = input("Enter a new password: ")

        if len(password1) < 8 or len(password1) > 12:
            print("Error: Password must be between 8 and 12 characters long.")
            continue

        password2 = input("Enter the password again: ")

        if password1 == password2:
            print("Your password is set!")
            break
        else:
            print("Error: The two passwords do not match!")

set_password()
