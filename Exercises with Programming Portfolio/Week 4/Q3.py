'''Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur. '''

def greeting():
    name = input("Hello, what is your name? ")
    
    # Convert the first letter of the name to uppercase and the rest to lowercase
    name = name[0].upper() + name[1:].lower()
    print("Hello, %s. Good to meet you!" % name)

greeting()