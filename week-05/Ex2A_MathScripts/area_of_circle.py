# Alvie Ahmed
# Week 5 Exercise 2.A: Make calculations with Python
# Lab 2, Question 4: Area of Circle

import math

# -------------------------------------------------------------------------

# 4. How do you calculate the area of a circle?

# ---
# a) The diameter of a given circle is the same as the day of your birthday
#    (not the month, just the day). Figure out the formula, refresh your
#    recollection of the difference between diameter and radius, and figure
#    out what the script should look like.

# Example formulas: diameter = 11
#                   radius = diameter / 2 
#                   area = pi * radius^2

diameter = 11
radius = diameter / 2

area = math.pi * math.pow(radius, 2)

print ('The area of a circle with radius ' + format(radius, '.2f') + ' is ' + format(area, '.2f'))
