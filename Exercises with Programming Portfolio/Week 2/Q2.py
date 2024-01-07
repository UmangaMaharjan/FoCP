''' Write a program that prompts a user to enter a temperature in Celsius, and then
displays the corresponding temperature in Fahrenheit, like so:
Enter a temperature in Celsius: 32.5
32.5C is equivalent to 90.5F.'''

def convert_to_fahrenheit(celsius):
    fahrenheit = float(celsius * 9 / 5) + 32
    return fahrenheit

celsius_input = input("Enter a temperature in Celsius: ")
celsius = round(float(celsius_input), 2)

fahrenheit = convert_to_fahrenheit(celsius)

print(f"{celsius:.2f}C is equivalent to {fahrenheit:.2f}F.")