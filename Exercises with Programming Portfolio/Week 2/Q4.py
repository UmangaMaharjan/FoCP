''' A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over. '''

def distribute_sweets():
    sweets_per_pupil = sweets // pupils # Integer division
    sweets_left_over = sweets % pupils # Gives the remainder
    return sweets_per_pupil, sweets_left_over

sweets = int(input("Enter the number of sweets: "))
pupils = int(input("Enter the number of pupils: "))

sweets_per_pupil, sweets_left_over = distribute_sweets() # Function Calling

print("Each pupil gets %s sweets." % sweets_per_pupil)
print("There are %s sweets left over." % sweets_left_over)