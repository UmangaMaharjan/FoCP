''' Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error. '''

def set_password():
    password1 = input("Enter a new password: ")
    password2 = input("Enter the password again: ")

# Checking the two passwords
    if password1 == password2:
        print("Your password is set!")
    else:
        print("Error: The two passwords do not match!")

set_password() 