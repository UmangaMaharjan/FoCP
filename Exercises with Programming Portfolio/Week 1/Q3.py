'''Over the summer, temperatures in Yorkshire reached 38.4C. Write a program that
converts this value in Celsius to the equivalent temperature in Fahrenheit, and then
displays both. '''

def convert_to_fahrenheit():
    fahrenheit = float(celsius * 9 / 5) + 32
    return fahrenheit

celsius = 38.4  # Temperature in Celsius is given in the question

fahrenheit = convert_to_fahrenheit()

# %.1f displays just one value after the decimal point
print("The temperature in Celsius is %.1f°C." % celsius) 
print("The temperature in Fahrenheit is %.1f°F." % fahrenheit) 