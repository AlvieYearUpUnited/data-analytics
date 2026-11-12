# Alvie Ahmed
# Week 5 Exercise 2.A: Make calculations with Python
# Lab 2, Question 3: Tip Amount

# -------------------------------------------------------------------------

# 3. How do you calculate the tip amount on a restaurant bill given the tip
#    percentage?

# ---
# a) Figure out the formula and what the script would look like, making up 
#    example values as needed. (If you need inspiration, what was your
#    approximate restaurant bill the last time you ate at a restaurant?

#    Example formula: tip_amount = meal_bill * tip_percent

# ---
# b) Create the script in a file named tip_amount.py

meal_bill = 113.95
tip_percent = .20

tip_amount = meal_bill * tip_percent

print('The tip on a $' + format(meal_bill, '.2f') + ' restaurant bill is $' + format(tip_amount, '.2f'))