''' Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function. '''

def validate_integer(n):
    # Check if the number is within the range 0 to 100
    if 0 <= n <= 100:
        return True
    else:
        return False

# Test the function
print(validate_integer(42))  # This should return True
print(validate_integer(-3))  # This should return False
print(validate_integer(99))  # This should return True
print(validate_integer(-53))  # This should return False
