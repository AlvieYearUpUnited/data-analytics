# Alvie Ahmed
# Week 5 Exercise 4.B: Lookups and greetings
# Lab 1, Question 2

# -------------------------------------------------------------------------

# 2. Once your script is working, rewrite it using a match/case statement 
#    instead of if/elif/else. Save this version as dept_converter_v2.py

print(f'Department Codes: |1|5|10|12|18|20|')
dept_id = int(input('Enter Department ID: '))

match dept_id:
    case 1:
        dept_name = 'Marketing'

    case 5:
        dept_name = 'Human Resources'

    case 10:
        dept_name = 'Accounting'

    case 12:
        dept_name = 'Legal'

    case 18:
        dept_name = 'IT'

    case 20:
        dept_name = 'Customer Relations' 

    case other:
        dept_name = 'INVALID'

print(f'Selected Department: {dept_name}')
    