# Alvie Ahmed
# Week 5 Exercise 3.B: Creating collections
# Lab 1: 

# ----------------------------------------------------------------------------

# 1. Create a file with the name movie_list.py. 

#2. Create a list with the titles of your favorite movies (or movies you’d like to watch) –
#   include at least 2, but no more than 10.

movies = ['spiderman', 'batman', 'superman', 'john wick']

# 3. Use the len() function to print the descriptive statement:
# The list [list name] includes my top [length] favorite movies
# (Or: The list [list name] includes the [length] movies I’d like to watch)
# Then use another line of code to print the complete list

# print(f'The list "movies" includes my top {len(movies)} favorite movies')

print(f'The list \'movies\' includes the the {len(movies)} movies I\'d like to watch') 
print(movies)
print()

# 4. Print a sorted list two ways (Note: make sure that your list items aren’t already in
# alphabetical order to start with, or you won’t notice any difference):

# a) Use the sorted() function to print a sorted list, then print the list again without
#    using sorted(). Example: print(sorted(listname)) | print(listname)
#    What do you notice when you compare the two outputs?

print(sorted(movies)) # My list is in alphabetical order for only this output
print(movies)         # My output lists the movie names in the order it was added 
print() 

# b) Use the .sort() method to sort the list, then print the list again, like this: 
#    listname.sort() | print(listname)
#    What do you notice when you compare the two outputs?

movies.sort() # Using .sort(), my list is output in alpabetical order for the rest
print(movies) # of my script. I won't need to use sort functions again moving forward 
print() 
print(movies)
# 5. Think of at least one more movie to add to your list, and use the .append() method to
#    add it. Then print the list again, also including an updated description statement.

movies.append('avengers')
print(f'The list \'movies\' includes the {len(movies)} movies I\'d like to watch')
print(movies)
print() # Correction: .sort() orders your list in alphabetical order for only 
        #             the current listed items. Newly added items aren't
        #             automatically sorted and you would need to use sort
        #             functions again. 



