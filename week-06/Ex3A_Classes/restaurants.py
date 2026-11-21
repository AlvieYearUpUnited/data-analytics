# Alvie Ahmed
# Week 6 Exercise 3.A: Working with classes
# Lab 1

# -------------------------------------------------------------------------

class Restaraunt:                                      # Creating class
    '''Restaraunt Food Type'''                         # Docstring description

# Initializing instance attributes
    def __init__(self, rest_name, food_type):           
        self.rest_name = rest_name
        self.food_type = food_type
# Creating methods within class
    def describe_rest(self):       
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):                      
        print(f'{self.rest_name} is open.')

# Creating instances for class
mcdonalds = Restaraunt('McDonalds', 'burgers') 

dunkin_donuts = Restaraunt('Dunkin Donuts', 'donuts')

chipotle = Restaraunt('Chipotle', 'protein bowls')

# Calling method for each instance
mcdonalds.describe_rest()
mcdonalds.rest_open()

dunkin_donuts.describe_rest()
dunkin_donuts.rest_open()

chipotle.describe_rest()
chipotle.rest_open()





    