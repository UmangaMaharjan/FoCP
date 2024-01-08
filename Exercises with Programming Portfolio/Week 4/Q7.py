'''Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean. '''

def convert_to_fahrenheit(celsius):
    fahrenheit = float(celsius * 9 / 5) + 32
    return fahrenheit

temperatures_celsius = []
for i in range(6):
    celsius_input = input(f"Enter temperature {i+1} in Celsius (e.g., 25.00C): ")
    celsius = round(float(celsius_input[:-1]), 2)
    temperatures_celsius.append(celsius)

temperatures_fahrenheit = [convert_to_fahrenheit(temp) for temp in temperatures_celsius]

max_temp = max(temperatures_fahrenheit)
min_temp = min(temperatures_fahrenheit)
mean_temp = sum(temperatures_fahrenheit) / len(temperatures_fahrenheit)

print(f"Maximum temperature: {max_temp:.2f}F")
print(f"Minimum temperature: {min_temp:.2f}F")
print(f"Mean temperature: {mean_temp:.2f}F")
