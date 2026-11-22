# Alvie Ahmed
# Week 6 Exercise 4.A: Practicing read/write
# Lab 1, PART 1

# -------------------------------------------------------------------------

f = open('about_me.txt', 'a')   # Initially used 'x' to create the file
                                # but then switched to 'a' to append
                
f.write('\n\nPerfect night out: Spending time with friends on a nice rooftop during nice weather') 

f.close()