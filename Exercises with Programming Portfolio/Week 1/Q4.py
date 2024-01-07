'''In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
times, was not out 162 times, and scored 48426 runs. Write a program to calculate
and display Boycott's batting average.'''

def calculate_batting_average(runs, times_batted, not_out):
    batting_average = runs / (times_batted - not_out)
    return batting_average

# Stats a/c to question
matches = 609
times_batted = 1014
not_out = 162
runs = 48426

batting_average = calculate_batting_average(runs, times_batted, not_out) # Calling the function

print ("Geoffrey Boycott's batting average is %.2f" % batting_average)