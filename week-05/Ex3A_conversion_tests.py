# Alvie Ahmed
# Week 5 Exercise 3.A: Numeric conversion exercises

# ----------------------------------------------------------------------------

# 1. Add a comment to the top using the following format:

# Description: This script tests various numeric
#              conversion techniques
# Author: Sam Q. Newprogrammer


# 2. Define the following variables:

a = " 101.1 " 
b = '55' 
c = "402 Stevens" 
d = 'Number 5 ' # string variable 

print (type(a))
print (type(b))
print (type(c))
print (type(d))

# ----------------------------------------------------------------------------
# 3. For each variable above, perform the following transformations, 
#    creating a new variable for each.

a_new = float(a)          
b_new = int(b)        
# c_new = int(c)        # 'ValueError' recieved when cast as int()
# d_new = float(d)      # 'ValueError' recieved when cast as float()

# ----------------------------------------------------------------------------
# 4. Once you have all new variables created (and error-producing lines
#    commented out), print the value of each variable and its type
#    - e.g., print (a, type(a))

print (a_new, type(a_new)) 
print (b_new, type(b_new))
# print (type(c_new))
# print (type(d_new))

# ----------------------------------------------------------------------------
# 5. For each variable, what happens when you try the following? Add comments 
#    to your script to document each result.

# ---
# a) Cast as integer using int()
 
print (int(a_new)) # int(a_new): '101' due to variable being previously 
#                                 casted as float
print (int(b_new)) # int(b_new): '55'
print (int(c_new)) # 'ValueError' due to containing letters 
print (int(d_new)) # 'ValueError' due to containing letters 

# ---
# b) Cast as float using float()

print(float(a_new)) # a_new: 101.1
print(float(b_new)) # b_new: 55.0
print(float(c_new)) # 'Value error' due to containing letter
print(float(d_new)) # 'Value error' due to containing letter

                    # c_new, d_new: 'Value error' due to containing letter

# ---
# c) For variable a, try casting into a float then integer, 
#    like this: int(float(a))

int(float(a))

#    int(float(a)) outputs '101'. It is being initially casted as a float(),
#    then casted as int() afterwards, giving us a valid output 

# ---
# d) Use slicing to add just the numeric portion of the string to a new variable
#    (remember, indexing always starts with 0!), and cast the number as an integer or
#    string, whichever is appropriate