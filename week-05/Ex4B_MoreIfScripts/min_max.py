# Alvie Ahmed
# Week 5 Exercise 4.B: Lookups and greetings
# Lab 4

# -------------------------------------------------------------------------

# 1. Create a script named min_max.py that displays both the smallest and 
#    then the largest of three numbers.
#    Name your variables a, b, and c and assign them values. Then use if/else
#    statement to determine and display the answer.
#    Be sure to test your script using an assortment of different values in your variables, so
#    that you look at a variety of different number combinations

a = 45
b = 45
c = 45

if a > b:
    if a > c:
        if c > b:
            print(f'Max: {a}')
            print(f'Min: {b}')
        else:
            print(f'Max: {a}')
            print(f'Min: {c}')
    else:
        print(f'Max: {c}')
        print(f'Min: {b}')
        
elif a < b:
    if b > c:
        if a > c:
            print(f'Max: {b}')
            print(f'Min: {c}')
        else:
            print(f'Max: {b}')
            print(f'Min: {a}')
    else:
        print(f'Max: {c}')
        print(f'Min: {a}') 

else: 
    if c > a:
        print(f'Max: {c}')
        print(f'Min: {a}')
    else:
        print(f'Max: {a}')
        print(f'Min: {c}')




