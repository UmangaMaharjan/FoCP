'''The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is 24 students, since this is the
number of PCs in a lab. Write a program that calculates how many groups are
needed for the following number of students: 113, 175, 12. Display how many full
groups there will be, and how many students will be in the smaller "left over"
group.'''

def calculate_groups(students):
    lab_group_size = 24
    full_groups = students // lab_group_size
    leftover_students = students % lab_group_size
    return full_groups, leftover_students

student_counts = [113, 175, 12]

for count in student_counts:
    full_groups, leftover_students = calculate_groups(count)
    print(f"For {count} students:")
    print(f"Full groups: {full_groups}")
    print(f"Leftover students: {leftover_students}\n")