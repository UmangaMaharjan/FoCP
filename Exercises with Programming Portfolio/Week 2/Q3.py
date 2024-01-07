'''
The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is usually 24 students, but this is
sometimes varied to create groups of similar size. Write a program that prompts for
the number of students and group size, and then displays how many groups will be
needed and how many will be left over in a smaller group.
How many students? 113
Required group size? 22
There will be 5 groups with 3 students left over.
For bonus credit, see if you can fix the grammar in the output. So if there were 101
students in groups of 20 the output would be:
There will be 5 groups with 1 student left over. '''

def calculate_groups(students, group_size):
    full_groups = students // group_size
    leftover_students = students % group_size
    return full_groups, leftover_students

students = int(input("How many students? "))
group_size = int(input("Required group size? "))

full_groups, leftover_students = calculate_groups(students, group_size)

student_word = "student" if leftover_students == 1 else "students"
group_word = "group" if full_groups == 1 else "groups"

print(f"There will be {full_groups} {group_word} with {leftover_students} {student_word} left over.")