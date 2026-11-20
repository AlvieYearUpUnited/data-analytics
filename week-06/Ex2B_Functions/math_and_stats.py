# Alvie Ahmed
# Week 6 Exercise 2.B: Using libray functions
# Lab 3

# -------------------------------------------------------------------------

import random
import math
import statistics

# Creating variables using imported modules
vals_1_100 = range(1,100) 
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

# Calculating sum, mean, median, of 75 random numbers
sum_75 = math.fsum(vals_sample)
avg_75 = statistics.mean(vals_sample)
med_75 = statistics.median(vals_sample)

# Calculating average, median, mode, standard deviation, and variance
# of 200 random numbers
avg_200 = statistics.mean(vals_choices)
med_200 = statistics.median(vals_choices)
mode_200 = statistics.mode(vals_choices)
stdev_200 = statistics.stdev(vals_choices)
var_200 = statistics.variance(vals_choices)

# Calculating circle's area
area_up = (math.ceil(math.pi * math.pow(radius, 2)))
area_down = (math.floor(pi * math.pow(radius, 2)))

print(f'\n_Experimenting with a subset of integers 1-100:')
print(f'Sum of 75 sample values from 1 to 100: {sum_75:,.2f}') 
print(f'Average of 75 sample values: {avg_75:.2f}')     
print(f'Median of 75 sample values: {med_75}\n')

print(f'_Experimenting with a superset of 200 values, integers 1-100: ')
print(f'Average of 200 values: {avg_200:.2f}')
print(f'Median of 200 values: {med_200}')
print(f'Mode of 200 values: {mode_200}')
print(f'Standard deviation of 200 values: {stdev_200:.2f}')
print(f'Variance of 200 values: {var_200:.2f}\n')

print(f'_Modeling a random circle:')
print(f'Radius = {radius}, area = {area_up} (rounded up to the nearest integer)')
print(f'Radius = {radius}, area = {area_down} (rounded down to the nearest integer)\n')





