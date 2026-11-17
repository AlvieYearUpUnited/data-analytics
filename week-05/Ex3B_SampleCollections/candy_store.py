# Alvie Ahmed
# Week 5 Exercise 3.B: Creating collections
# Lab 2: Candy Store

# ----------------------------------------------------------------------------

# 1. Create a script named candy_store.py. 
# 2. Start by creating two tuples: one that lists at least 3 types of candy 
#    that can come in fruit flavors, and another that lists at least 3 fruity 
#    flavors. (Feel free to get creative with your flavor ideas…) 

fruit_candy = ('sour patch', 'nerds', 'skittles')

fruit_flavors = ('strawberry', 'orange', 'grape')

# 3. Now create a new variable to store candy combinations as a set. Using the
#    index of each tuple, add at least one combination of each candy and flavor
#    to the new set – for example, putting together tuple1[0] and tuple2[1]

candy = set()

candy.add(f'{fruit_flavors[0]} {fruit_candy[0]}')
candy.add(f'{fruit_flavors[1]} {fruit_candy[1]}')
candy.add(f'{fruit_flavors[2]} {fruit_candy[2]}')

# 4. Create an output message that says, “Today’s candy options include:” and 
#    then prints the contents of the set.

print(f'Today\'s candy options include: {candy}')

# 5. 5. Print the output multiple times. What do you notice about the order
#       of the items as you repeat the output?

#       The order is constantly changing, since sets are unordered