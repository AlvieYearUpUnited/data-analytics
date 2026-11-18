# Alvie Ahmed
# Week 5 Exercise 4.B: Lookups and greetings
# Lab 3

# -------------------------------------------------------------------------

# 1. Create a script named complex_taxes.py that will calculate federal 
#    tax based on the values of annual gross income (a number) and a 
#    filing status (‘single’ or ‘joint’).

# 2. Start by copying your code for calculation of gross pay from the earlier 
#    lab (pay_rules.py) and include it here as part of your starting point.
#    Remember, that code calculates weekly gross pay. Extend that calculation
#    to estimate annual gross pay (how many weeks in a year?) and save it to
#    a new variable.

pay_rate = float(input('Enter your hourly pay rate: $'))
weekly_hours_worked = float(input('Enter hours worked this week: '))

if weekly_hours_worked <= 40:
    regular_pay = pay_rate * weekly_hours_worked

overtime_pay = 0
if weekly_hours_worked > 40:
    regular_pay = pay_rate * 40
    overtime_pay = (pay_rate * 1.5) * (weekly_hours_worked - 40)

weekly_gross_pay = regular_pay + overtime_pay
annual_gross_pay = weekly_gross_pay * 52

# 3. Use a series of if statements to determine the appropriate tax rate. 

print()
print('Single Filers: 1 | Joint Filers: 2')
filing_status_input = int(input('Enter filing status(1 or 2): '))

if filing_status_input == 1:
    filing_status = 'Single'
    if annual_gross_pay < 12000:
        tax_rate = .05
    elif annual_gross_pay  >= 12000 and annual_gross_pay < 25000:
        tax_rate = .10
    elif annual_gross_pay >= 25000 and annual_gross_pay < 75000:
        tax_rate = .15
    elif annual_gross_pay >= 75000:
        tax_rate = .20

elif filing_status_input == 2:
    filing_status = 'Joint'
    if annual_gross_pay < 12000:
        tax_rate = .00
    elif annual_gross_pay  >= 12000 and annual_gross_pay < 25000:
        tax_rate = .06
    elif annual_gross_pay >= 25000 and annual_gross_pay < 75000:
        tax_rate = .11
    elif annual_gross_pay >= 75000:
        tax_rate = .20

# 4. Use the tax rate to determine the tax withheld from the weekly gross pay
annual_withheld = annual_gross_pay * tax_rate
weekly_withheld = annual_withheld / 52
weekly_net_pay = weekly_gross_pay - weekly_withheld


#5. Create separate print statements to print the relevant information 
#   determined by the above calculations.

print()
print(f'You worked {weekly_hours_worked} this period.')
print(f'Because you earn {pay_rate} per hour, your gross weekly pay is ${weekly_gross_pay:,.2f}')
print(f'Your filing status is {filing_status}')
print(f'Your tax withholding for the week is ${weekly_withheld:,.2f}')
print(f'Your net pay is ${weekly_net_pay:,.2f}')





