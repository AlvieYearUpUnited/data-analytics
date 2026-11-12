# Alvie Ahmed
# Week 5 Exercise 2.B: More practical math scripts
# Lab 1, Question 1: Fahrenheit to Celsius

# -------------------------------------------------------------------------

# 1. How do you convert a temperature from Fahrenheit to Celsius?
#    Create the script in a file named f_to_c.py

# Example function: celsius = (fahrenheit - 32) * (5 / 9)

f = float(input('Enter a temperature in Fahrenheit: '))

c = (f - 32) * (5 / 9)

print (f'{f:.2f} degrees Fahrenheit is equivalent to {c:.2f} degrees Celsius')

