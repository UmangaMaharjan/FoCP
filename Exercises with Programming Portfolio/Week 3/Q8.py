''' Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times". '''

def times_table():
    # Ask the user for a number
    num = int(input("Enter a number: "))

    if -12 <= num <= 12:
        # If the number is negative, print the times table backwards
        if num < 0:
            for i in range(12, -1, -1):
                print("%d x %d = %d" % (i, -num, i * -num))
        # If the number is positive, print the times table normally
        else:
            for i in range(13):
                print("%d x %d = %d" % (i, num, i * num))
    else:
        print(" Please enter a number between -12 and 12!")

times_table()