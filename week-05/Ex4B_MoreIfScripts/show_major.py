# Alvie Ahmed
# Week 5 Exercise 4.B: Lookups and greetings
# Lab 5

# -------------------------------------------------------------------------

student_name = input('Enter Student Name: ')
student_major = input('Enter Student Major Code: ').strip().upper()

if student_major == 'BIOL':
    major_name = 'Biology'
    department_office = 'Science Bldg, Room 310'

elif student_major == 'CSCI':
    major_name = 'Computer Science'
    department_office = 'Sheppard Hall, Room 314'

elif student_major == 'ENG':
    major_name = 'English'
    department_office = 'Kerr Hall, Room 201'

elif student_major == 'HIST':
    major_name = 'History'
    department_office = 'Kerr Hall, Room 114'

elif student_major == 'MKT':
    major_name = 'Marketing'
    department_office = 'Westly Hall, Room 310'

else:
    major_name = '<unknown>'
    department_office = ''

print(f'Student Name: {student_name}')
print(f'Student Major: {major_name}')
print(f'Department Office Location: {department_office}')