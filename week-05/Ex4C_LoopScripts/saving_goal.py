# Alvie Ahmed
# Week 5 Exercise 4.C: Loop de loop
# Lab 2

# -------------------------------------------------------------------------

# 1. Create a script named savings_goal.py.

# 2. Create a variable for your starting bank balance, another that sets 
#    your savings goal, and a third with your weekly savings amount.

bank_balance = 1000    
savings_goal = 3000    
weekly_savings = 200   

treat = 50                       

# 3. Use a while loop to compare your bank balance to your savings goal,
#    if you haven’t met your goal yet, add the weekly savings amount to 
#    your bank balance. For each loop, print the statement, 
#    “This week my balance increased to ___.” Once your savings goal
#     is met, print the statement, “Goal met! My current balance is ___.”

while bank_balance < savings_goal:
        bank_balance += weekly_savings

        if bank_balance >= savings_goal * .75:
                bank_balance -= treat
                if bank_balance >= savings_goal:
                    break
                print(f'So close! After treating myself, my balance is up to ${bank_balance:,.2f}')
                
        elif bank_balance > savings_goal / 2:
                print(f'Almost there! This week my balance is up to ${bank_balance:,.2f}')
        else:
            print(f'This week my balance increased to ${bank_balance:,.2f}')

print(f'Goal met! My current balance is ${bank_balance:,.2f}')


# 4. Try adding additional logic to your loop:

# a) If your balance is more than halfway to your goal,
#    print the message, “Almost there! This week my balance is up to ___.”

#    Lines 33-34

# b) If your balance is at least 75% of your goal, add a calculation to
#    buy yourself a little treat. Print the message, 
#    “So close! After treating myself, my balance is up to ___.”

#    Line 16, Lines 27-31


