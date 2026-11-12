# Alvie Ahmed
# Week 5 Exercise 2.A: Make calculations with Python
# Lab 2, Question 5: Rule of 72

# -------------------------------------------------------------------------

# 4. How long will it take a savings account worth X to double in value 
#    based on an interest rate of IR? (Hint: Look up the “rule of 72”)

# ---
# a) Figure out the formula and what the script would look like, 
#    making up example values as needed.

# Example Formula: years = 72 / IR

# ---
# b) Create the script in a file named rule_of_72.py

X = 15000
IR = .06

doubleX = 2 * X
years = 72 / (IR * 100)

print ('Your current saving is ' + format(X, '.2f') + '.')

# print ('At a ' + format(IR, '.2f') 
#       + '% interest rate, your savings account will be worth '  
#       + format(doubleX, '.2f') + ' in ' + format(years, '.1f') + ' years'
#       )

# ---
# e) There are a couple ways you might get the interest rate to display as
#    a percentage. One option is to use the format function. In this case,
#    instead of including the character f to assign a fixed decimal format, 
#    use the character % to assign the percentage format, 
#    e.g. format(__, ".0%")    

print ('At a ' + format(IR, '.0%')
      + ' interest rate, your savings account will be worth '
      + format(doubleX, '.2f') + ' in ' + format(years, '.1f') + 'years'
      )


