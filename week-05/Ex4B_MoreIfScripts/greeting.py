# Alvie Ahmed
# Week 5 Exercise 4.B: Lookups and greetings
# Lab 2

# -------------------------------------------------------------------------

# 1. Create a script named greeting.py. Define a variable that contains the
#    current hour (0-23). Display one of the greetings below based on 
#    the current hour:

time = int(input(f'Enter Current Hour (Military Time): '))

if time >= 0 and time < 10:
    greeting = 'Good morning!'

elif time >= 10 and time < 17:
    greeting = 'Good day!'

elif time >= 17 and time <= 23:
    greeting = 'Good evening!'

else:
    greeting = 'Error!'

print(greeting)

if time >= 0 and time < 4 or time == 23:  

    print('What are you doing up so late??')

