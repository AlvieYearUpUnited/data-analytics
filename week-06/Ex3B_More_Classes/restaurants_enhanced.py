# Alvie Ahmed
# Week 6 Exercise 3.B: More fun with classes
# Lab 1

# -------------------------------------------------------------------------
import statistics

class Restaurant:                                      # Creating class
    '''Restaurant Food Type'''                         # Docstring description

# Initializing instance attributes
    def __init__(self, rest_name, food_type):           
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

# Creating methods within class
    def describe_rest(self):       
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):                      
        print(f'{self.rest_name} is open.')

    def add_num_served(self):
        self.number_served += int(input(f'How many {self.rest_name} customers served today?: '))

    def print_num_served(self):
        print(f'{self.rest_name} has served {self.number_served} customers.')

    def customer_rating(self):
        while True:
            try:

                rating = int(input(f'How would you rate your experience today on a scale of 1-5 (5 being excellent)?: '))

                if rating >= 1 and rating <= 5:
                    self.customer_ratings.append(rating)
                    avg_rating = statistics.mean(self.customer_ratings)
                  # avg_rating = sum(self.customer_ratings) / len(self.customer_ratings) 
                    print(f'Your rating was {rating}. The average rating for this restaurant is {avg_rating}')
                    break
                else:
                     print(f'\nEnter a number 1-5: ')
            
            except ValueError:

                print(f'\nPlease enter a whole number: ')
                

# Creating instances for class
mcdonalds = Restaurant('McDonalds', 'burgers') 

dunkin = Restaurant('Dunkin Donuts', 'donuts')

chipotle = Restaurant('Chipotle', 'protein bowls')

# Calling method for each instance
mcdonalds.describe_rest()
mcdonalds.rest_open()

dunkin.describe_rest()
dunkin.rest_open()

chipotle.describe_rest()
chipotle.rest_open()

mcdonalds.print_num_served()
dunkin.print_num_served()
chipotle.print_num_served()

mcdonalds.add_num_served()
mcdonalds.add_num_served()

dunkin.add_num_served()
dunkin.add_num_served()

chipotle.add_num_served()
chipotle.add_num_served()

mcdonalds.print_num_served()
dunkin.print_num_served()
chipotle.print_num_served()

mcdonalds.customer_rating()
mcdonalds.customer_rating()
dunkin.customer_rating()
dunkin.customer_rating()
chipotle.customer_rating()
chipotle.customer_rating()