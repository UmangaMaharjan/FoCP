import getpass

# Function to check if a username already exists
def check_existing_username(username):
    with open('passwd.txt', 'r') as file:

        existing_usernames = []

        # For reading each line from the file
        for line in file.readlines():
            # Split the line at the colon and take the first part
            existing_username = line.split(':')[0]
            existing_usernames.append(existing_username)
        return username in existing_usernames

# Function to add a new user
def add_user(username, real_name, password):
    if check_existing_username(username):
        print("\nError! Username already exists. Please try again!")
    else:
        with open('passwd.txt', 'a') as file:
            file.write(f"{username}:{real_name}:{password}\n")
        print("\nUser Created!")

# Function to log in with username and password
def login(username, password):
    with open('passwd.txt', 'r') as file:
        for line in file:
            u, _, p = line.strip().split(':')
            if u == username and p == password:
                print("\nAccess granted.")
                return

    print("\nAccess denied.")

# Function to change user password
def change_password(username, current_password, new_password):
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()

    found = False
    with open('passwd.txt', 'w') as file:
        for line in lines:
            if line.startswith(f"{username}:") and line.endswith(f":{current_password}\n"):
                found = True
                file.write(f"{username}:{line.split(':')[1]}:{new_password}\n")
            else:
                file.write(line)

    if found:
        print("\nPassword changed.")
    else:
        print("\nError! User not found or current password is incorrect.")

# Function to delete a user
def delete_user(username):
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()

    found = False
    with open('passwd.txt', 'w') as file:
        for line in lines:
            if not line.startswith(f"{username}:"):
                file.write(line)
            else:
                found = True

    if found:
        print("\nUser Deleted.")
    else:
        print("\nError! User not found. Try Again!")

def menu():
    print("\nInteractive Account Management System")
    print("=====================================")
    print("1. Add User")
    print("2. Login")
    print("3. Change Password")
    print("4. Delete User")
    print("5. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")
           

        if choice == '1':
            print("\n>ADD AN USER<")   
            username = input("Enter new username: ")
            real_name = input("Enter real name: ")
            password = getpass.getpass("Enter password: ")
            add_user(username, real_name, password)

        elif choice == '2':
            print("\n>LOGIN<")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login(username, password)

        elif choice == '3':
            print("\n>CHANGE PASSWORD<")
            username = input("Enter your username: ")
            current_password = input("Enter your current password: ")
            new_password = input("Enter your new password: ")
            confirm_password = input("Confirm your new password: ")

            if new_password == confirm_password:
                change_password(username, current_password, new_password)
            else:
                print("Passwords do not match. Nothing changed.\n")

        elif choice == '4':
            print("\n>DELETE AN USER<")
            username = input("Enter your username: ")
            delete_user(username)

        elif choice == '5':
            print("\nGoodbye!!\n")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 5!") 