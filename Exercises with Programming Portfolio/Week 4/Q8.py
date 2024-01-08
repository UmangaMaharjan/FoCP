''' Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value. '''

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Read temperatures in Celsius until the user just presses "Enter"
temps_c = []
while True:
    temp_c = input("Enter temperature in Celsius, or press Enter to finish: ")
    if temp_c == "":
        break
    temps_c.append(temp_c)

# Convert temperatures to Fahrenheit and remove the 'C'
temps_f = [celsius_to_fahrenheit(float(temp[:-1])) for temp in temps_c]

# Calculate max, min, and mean if any temperatures were entered
if temps_f:
    max_temp = max(temps_f)
    min_temp = min(temps_f)
    mean_temp = sum(temps_f) / len(temps_f)

    print("Max: %.1fF\nMin: %.1fF\nMean: %.1fF" % (max_temp, min_temp, mean_temp))
else:
    print("No temperatures were entered.")