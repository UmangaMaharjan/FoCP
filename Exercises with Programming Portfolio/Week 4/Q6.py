''' Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format. '''

def convert_to_fahrenheit(celsius):
    fahrenheit = float(celsius * 9 / 5) + 32
    return fahrenheit

celsius_input = input("Enter a temperature in Celsius (e.g., 25.00C): ")
celsius = round(float(celsius_input[:-1]), 2)

fahrenheit = convert_to_fahrenheit(celsius)

print(f"{celsius:.2f}C is equivalent to {fahrenheit:.2f}F.")