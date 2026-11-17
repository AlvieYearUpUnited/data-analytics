# Alvie Ahmed
# Week 5 Exercise 4.A: Using conditionals
# Lab 2: Pay Rules

# -------------------------------------------------------------------------

# 1. In a file named pay_rules.py, create a script to calculate gross pay
#    given the variables pay_rate and hours_worked. If the person works more
#    than 40 hours, pay the overtime hours at 1.5 times the rate of regular 
#    hours.

pay_rate = float(input('Enter your hourly pay rate: $'))
hours_worked = float(input('Enter hours worked: '))

if hours_worked <= 40:
    regular_pay = pay_rate * hours_worked

overtime_pay = 0
if hours_worked > 40:
    regular_pay = pay_rate * 40
    overtime_pay = (pay_rate * 1.5) * (hours_worked - 40)

gross_pay = regular_pay + overtime_pay

print(gross_pay)



                 
                 
                 