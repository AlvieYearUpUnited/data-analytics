# Alvie Ahmed
# Week 5 Exercise 4.C: Loop de loop
# Lab 3

# -------------------------------------------------------------------------

# 1. Create a script named ranked_list.py.
# 2. Create a list of at least 5 items using anything you like: 
#    favorite foods, pets, cities you'd like to visit, 
#    skills you want to develop, etc.

foods = ['pizza', 'burger', 'pasta', 'sushi', 'wings']

# 3. Use enumerate() with a for loop to print each item as a 
#    numbered list, starting at 1.

# 4. Now add an if statement inside your loop: if the 
#    index is 1 (i.e., the first item), also 
#    print " <- top pick!" on the same line.

for i, f in enumerate(reversed(foods), start=1):
    if i == 1:
        print(f'{i}. {f} <- top pick!')

    else:
        print(f'{i}. {f}')

# 5. BONUS: Modify your loop to print the list in 
#    reverse order (still numbered 1 through 5) 
#    using reversed() around your list. 