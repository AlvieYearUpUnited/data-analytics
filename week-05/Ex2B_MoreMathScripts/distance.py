# Alvie Ahmed
# Week 5 Exercise 2.B: More practical math scripts
# Lab 1, Question 4: Coordinate Distance

# -------------------------------------------------------------------------

# 4. How do you calculate the distance between coordinates 
#    (x1, y1) and (x2, y2)? 
#    Hint: You'll need to look up how to calculate a square root in Python, 
#    which may involve a function from the math module.
#    Code the script for calculating this distance in a file named distance.py

import math

x1 = 4 
y1 = 2

x2 = 6 
y2 = 8

y_diff = y2 - y1 # difference in y-axis
x_diff = x2 - x1 # difference in x-axis

# Pythagoreon Theorom c^2 = a^2 + b^2
# Using both math.pow() and ** to help understand that both calculate exponents
distance = math.sqrt(math.pow(y_diff, 2) + x_diff ** 2) 

print (f'Coordinates: ({x1}, {y1}), ({x2}, {y2})')
print (f'\nDistance between coordinates: {distance:.2f}')
