# Alvie Ahmed
# Week 5 Exercise 4.C: Loop de loop
# Lab 1

# -------------------------------------------------------------------------

# 1. Create a script named loop_love.py.

# 2. Create a list of words that mean great such as amazing, awesome, 
#    excellent, etc.

great_words = ['amazing', 'awesome', 'fantastic', 'excellent']

# 3. Use a for loop to iterate through your list, and with each loop print
#    out the phrase “Loops are ____!” filling in the blank with a word 
#    from the list.

for i in range(len(great_words)):
    print(f'Loops are {great_words[i]}')


# 4. When your loop has finished, print the additional phrase “I <3 loops”

print(f'I <3 loops') 
