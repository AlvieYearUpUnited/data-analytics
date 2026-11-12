# Alvie Ahmed
# Week 5 Exercise 2.B: More practical math scripts
# Lab 1, Question 3: Withheld Taxes

# -------------------------------------------------------------------------

#3. Federal taxes are 23% of your salary every month. You make X amount 
#   of money. How much is withheld for taxes?
#   Code the script in a file named taxes.py

salary = 85000                            # Annual Salary
fed_tax = .23

m_withheld = (salary / 12) * fed_tax      # Monthly Witheld Amount
y_withheld = salary * fed_tax             # Yearly Withheld Amount

print ('\n         FEDERAL TAX WITHELD')
print ('----------------------------------------')

print ('  Annual Salary: $' + format(salary, ',.2f'))
print ('Monthy Withheld:  $' + format(m_withheld, ',.2f'))
print ('Yearly Withheld: $' + format(y_withheld, ',.2f'))


# I found the question to be unclear as it did not state how often you make
# X amount of money, and it also did not clarify if it was asking for total
# withheld per month or per year. 
# Due to this, I created two variables, one for monthly withheld and one 
# for yearly withheld.


