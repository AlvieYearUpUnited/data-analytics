# Alvie Ahmed
# Week 5 Exercise 2.B: More practical math scripts
# Lab 1, Question 6: Van Rentals

# -------------------------------------------------------------------------

# 6. There are X people going on a tour. Charter vans seat 15 passengers 
#    each. Vans cost $250 per day to rent (including the driver’s pay). 
#    How many vans do you need? How much will it cost to rent vans? 
#    What is the cost if you split it per person?
#    Code the script in a file named rentals.py

import math

tourists = int(input('Enter amount of people going on tour: '))

van_dailycost = 250
vans_required = math.ceil(tourists / 15)
rental_cost = vans_required * van_dailycost
cost_per_person = round(rental_cost / tourists, 2)

print (f'\nTourists Count: {tourists}')
print (f'Vans Required:   {vans_required}')
print ('-----------------------------------------')
print (f'Total Rental Cost: ${rental_cost:,.2f}')
print (f'Cost Per Person:    ${cost_per_person}')

# a) How much money did your script say you had to charge per person?

#    $19.74 per person

# ---
# b) If you multiply that out, how much did you collect?

#    $19.74 * 38 = $750.12

# ---
# c) How much were the vans?

#    $750.00

# ---
# d) Why do you have leftover money?

#    We have leftover money because we rounded the cost per person. 
#    750 divided by 38 is 19.736842 but we rounded it out to 19.74. 
#    This led to each person paying slightly more, leaving us with
#    an extra 12 cents.
 



