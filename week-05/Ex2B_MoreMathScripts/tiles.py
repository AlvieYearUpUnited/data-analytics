# Alvie Ahmed
# Week 5 Exercise 2.B: More practical math scripts
# Lab 1, Question 5: Tile Boxes to Purchase

# -------------------------------------------------------------------------

# 5. You are going to tile a room whose dimensions are length by width
#    feet. There are twelve tiles per box, each 1 foot by 1 foot. 
#    How many boxes of tiles do you need? You can only buy full boxes, 
#    not a partial box.

#    You also want to buy at least 10% more tiles than you need in 
#    order to handle chips, breakage, and mess-ups. 
#    How many total boxes will you buy?

#    Code the script in a file named tiles.py

import math

room_length = 12
room_width = 6

room_area = room_length * room_width

tile_length = 1
tile_width = 1
tile_area = tile_length * tile_width

tilebox_coverage =  tile_area * 12

required_count = room_area / tilebox_coverage

ten_percent = required_count * .10

purchase_count = required_count + ten_percent

print ('\nTiles Per Box: 12 | Tile Dimensions: ' + str(tile_length) + 'x' + str(tile_width) + ' feet')
print ('-------------------------------------------------')

print ('Room Dimensions: ' + str(room_length) + 'x' + str(room_width) + ' feet')
print ('Room Area: ' + str(room_area) + ' square feet')
print ('Boxes required: ' + str(math.ceil(required_count)))
print ('Boxes to purchase: ' + str(math.ceil(purchase_count)))



