''' Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive. '''

def times_table():
    # Ask the user for a number between 0 and 12
    num = int(input("Enter a number between 0 and 12: "))

    # Check if the number is within the valid range
    if 0 <= num <= 12:
        # Print the times table for the entered number
        for i in range(13):
            print("%d x %d = %d" % (i, num, i * num))
    else:
        print("Please enter a number between 0 and 12!")

times_table()