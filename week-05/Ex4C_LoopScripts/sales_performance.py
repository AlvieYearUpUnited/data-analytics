# Alvie Ahmed
# Week 5 Exercise 4.C: Loop de loop
# Lab 4

# -------------------------------------------------------------------------

# 1. Create a script named sales_performance.py.
# 2. You have been given the following list of sales records. Each record 
#    is a tuple containing a salesperson's name, their region, and their
#    total sales for the month:

sales_data = [
    ('Marcus Webb',     'East',  4250.00),
    ('Pirya Sharma',    'West',  5875.50),
    ('DeShawn Carter',  'East',  3100.75),
    ('LaTonya Rivers',  'South', 6420.00),
    ('Bob Nguyen',      'West',  4980.25),
]

# 3. Use a for loop to unpack each tuple directly in the loop statement, 
#    and print a summary line for each record

for name, region, total_sales in sales_data:
    print(f'{name} ({region}): ${total_sales:,.2f}')

    if total_sales > 5000:
        print(f'^ Top performer!')
    