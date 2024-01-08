''' Modify your greeting program so that if the user does not enter a name (i.e. they
just press enter), the program responds "Hello, Stranger!". Otherwise it should print
a greeting with their name as before. '''

def greeting():
    name = input("Hello, what is your name? ")

    if name:
        print("Hello, %s. Good to meet you!" % name)
    else:
        print("Hello, Stranger!")

greeting()