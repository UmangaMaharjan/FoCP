''' Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. ''' 

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Testing the functions with user input
c = float(input("Enter temperature in Celsius: "))
print("%.1f Celsius is %.1f Fahrenheit" % (c, celsius_to_fahrenheit(c)))

print("\n")  # Adds a new line

f = float(input("Enter temperature in Fahrenheit: "))
print("%.1f Fahrenheit is %.1f Celsius" % (f, fahrenheit_to_celsius(f)))