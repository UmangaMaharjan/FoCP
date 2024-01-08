''' Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long. '''

def set_password():
    password1 = input("Enter a new password: ")

    # Checking password length
    if len(password1) < 8 or len(password1) > 12: 
        print("Error: Password must be between 8 and 12 characters long.")
        return
    password2 = input("Enter the password again: ")

# Checking the two passwords
    if password1 == password2:
        print("Your password is set!")
    else:
        print("Error: The two passwords do not match!")

set_password() 