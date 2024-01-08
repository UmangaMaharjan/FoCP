''' When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.) '''

def remove_last_character(input_string):
    # Check if the string has one or fewer characters
    if len(input_string) <= 1:
        return input_string

    # Remove the last character and return the modified string
    modified_string = input_string[:-1]
    return modified_string

# Test the function
user_input = input("Enter a string: ")
result = remove_last_character(user_input)

print("Original String:", user_input)
print("Modified String:", result)