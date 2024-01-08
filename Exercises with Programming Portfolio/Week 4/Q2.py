''' Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program. '''

def count_letters(s):
    # Initialize counters for uppercase and lowercase letters
    uppercase = 0
    lowercase = 0

    # Loop each character in the string
    for char in s:
        # If the character is an uppercase letter, increment the uppercase counter
        if 'A' <= char <= 'Z':
            uppercase += 1
        # If the character is a lowercase letter, increment the lowercase counter
        elif 'a' <= char <= 'z':
            lowercase += 1
    return uppercase, lowercase

test_string = "Let's Check the OUTPUT"
uppercase, lowercase = count_letters(test_string)
print("The string '%s' has %d uppercase letters and %d lowercase letters." % (test_string, uppercase, lowercase))