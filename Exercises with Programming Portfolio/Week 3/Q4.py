''' Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber'] '''

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

def set_password():
    password1 = input("Enter a new password: ")

    # Checking if password is in the list of bad passwords
    if password1 in BAD_PASSWORDS:
        print(f"Error: The password '{password1}' is too common. Please choose a different password.")
        return
    
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