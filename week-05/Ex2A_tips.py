

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
print ('The total due is ' + str(total_due))

# 2a)   The str function converts the total_due float value into a string 
#       so that it can be output with the rest of the string text within the
#       print statement. The + operator cannot concatenate a string with
#       a float variable.  

# ----------------------------------------------------------------------------

# 5)

print ('Food cost is ' + str(food_cost) + ' and tax is ' +str(tax))
# print ('Tip is ' + str(tip))
print ('Total due is ' + str(total_due))

print ('Tip is ' + format(tip, '.2f'))

