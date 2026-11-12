# Alvie Ahmed
# Week 5 Exercise 2.A

# -------------------------------------------------------------------------

# 1. How do you calculate your net worth given your assets and debts? 
# ---
# a) Start by brainstorming: What are “assets” that would need to be  
#    included in this calculation? What about “debts”?

# Required assets to include: Liquid Cash, Property, Cars
# Required debts to include: Credit Card, Mortgages, Auto Loans
# ---
# b) Discuss and figure out the formula and what the script would look  
#    like, making up example values as needed.

#    Example formula: net_worth = total_assets - total_debt
# ---
# c) Now create the script in a file named net_worth.py

liquid_cash = float(input('Enter total liquid cash owned: $'))
property = float(input('Enter total value for all properties owned: $'))
vehicles = float(input('Enter total value for all vehicles owned: $'))

total_assets = liquid_cash + property + vehicles

cc_debt = float(input('Enter your total credit card debt: $')) # Credit Card Debt
m_debt = float(input('Enter total balance owed on all mortgages: $')) # Mortgage Debt
al_debt = float(input('Enter total balance owed on all auto loans: $')) # Auto Loan Debt

total_debt = cc_debt + m_debt + al_debt

net_worth = total_assets - total_debt

print ('Your total assets are $' + format(total_assets, '.2f'))
print ('Your total debts are $' + format(total_debt, '.2f'))
print ('Your net worth is $' + format(net_worth, '.2f'))


