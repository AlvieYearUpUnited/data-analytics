# Alvie Ahmed
# Week 5 Exercise 4.B: Lookups and greetings
# Lab 1, Question 1

# -------------------------------------------------------------------------

# 1. Write a script named dept_converter.py that uses if/elif/else logic
#    to determine and print department name based on a department code. 
#    Make sure to test your script with multiple codes.

print(f'Department Codes: |1|5|10|12|18|20|')
dept_code = int(input(f'Enter department code: '))

if dept_code == 1:
    dept_name = 'Marketing'

elif dept_code == 5:
    dept_name = 'Human Resources'

elif dept_code == 10:
    dept_name = 'Accounting'

elif dept_code == 12:
    dept_name = 'Legal'

elif dept_code == 18:
    dept_name = 'IT'

elif dept_code == 20:
    dept_name = 'Customer Relations'

else:
    dept_name = 'INVALID'

print(f'Department Selected: {dept_name}')

    

