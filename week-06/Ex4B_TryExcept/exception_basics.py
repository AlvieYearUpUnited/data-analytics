# Alvie Ahmed
# Week 6 Exercise 4.B: Working with exceptions
# Lab 1

# -------------------------------------------------------------------------

# ValueError
try: 
    int_check = int(input('Enter an integer: '))
except ValueError:
    print(f'ValueError: Can\'t convert letters to integer')
else: 
    print(int_check)
finally:
    print(f'Let\'s try another one!')

# NameError
try:
    name_check = Alvie
except NameError:
    print(f'NameError: Variable \'Alvie\' not defined')
else: 
    print(name_check)
finally:
    print(f'Let\'s try another one!')

# TypeError
try:
    type_check = 'Hello'
    five = 5
    total = type_check + five
except TypeError:
    print(f'TypeError: String and integer cannot be added!')
else:
    print(total)
finally:
    print(f'Let\'s try another one!')

# SyntaxError
try:
    exec("if True print('Hello')") # Attempting to run string as actual code
except SyntaxError:
    print(f'SyntaxError: Colon forgotten after if statement.')
else:
    print('No SyntaxError!')

finally:
    print(f'And we\'re done!')
    

