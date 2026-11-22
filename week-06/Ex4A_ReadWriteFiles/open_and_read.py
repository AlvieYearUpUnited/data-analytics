
# Alvie Ahmed
# Week 6 Exercise 4.A: Practicing read/write
# Lab 1, PART 2

# -------------------------------------------------------------------------
f = open('about_me.txt', 'r')

# print(f.read(50))     # Reading first 50 characters
# print(f.read(50))     # Reading second 50 characters

# print(f.readline(10)) # Start from current position, read up to 10 characters in that line
# print(f.readline())   # Start from current postion, read until end of line

# for i in range(1, 5):
#     print(f.readline())

# print(f.readlines(1)) # Reads complete line, even when past character limit
# print(f.readlines(1)) # Returns list of strings, including \n as well
# print(f.readlines(10))
# print(f.readlines(10))
# print(f.readlines(100))
# print(f.readlines(-1))

first_50 = f.read(50)
next_four_lines = []

for i in range(1, 5):
    next_four_lines.append(f.readline())

next_100 = f.readlines(100)

print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {next_four_lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_100}")

f.close()

