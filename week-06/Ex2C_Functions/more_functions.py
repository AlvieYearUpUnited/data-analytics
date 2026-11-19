# Alvie Ahmed
# Week 6 Exercise 2.C: Creating and calling functions
# Lab 2

# -------------------------------------------------------------------------

# Function 1: Display mailing address
def display_mailing_label(name, address, city, state, zip):
    print(f'{name}')
    print(f'{address}')
    print(f'{city}, {state} {zip}')


print(f'\nMAILING ADDRESSES')
print(f'------------------')

display_mailing_label('Josh Williams', '341 Golly', 'Queens', 'NY', '11412')
print()
display_mailing_label('YearUp', '85 Broad Street', 'New York', 'NY', '10001')
print()


# --
# Function 2: Add all numbers and display entire equation
def add_numbers(*numbers):
    
    total = 0
    str_convert = ''

    for i in numbers:
        total += i

        if str_convert == '':
            str_convert = f'{i}'
        else:
            str_convert += f' + {i}'

    print(f'{str_convert} = {total}')

print(f'ADDING NUMBERS')
print(f'------------------')

add_numbers(4)
print()
add_numbers(8, 40)
print()
add_numbers(5, 10, 15, 20)
print()

# --
# Function 3: Display receipt, calculate change due
def display_receipt(total_due, amount_paid):
     
    if total_due > amount_paid:
        remaining_balance = total_due - amount_paid
        print(f'Total Due: ${total_due:,.2f}')
        print(f'Amount Paid ${amount_paid:,.2f}')
        print(f'\nRemaining Balance: ${remaining_balance:,.2f}')
    else:
        change_due = amount_paid - total_due
        print(f'Total Due: ${total_due:,.2f}')
        print(f'Amount Paid ${amount_paid:,.2f}')

        print(f'\nChange Due: ${change_due:,.2f}')


print(f'RECEIPT 1')
print(f'------------------')
display_receipt(85.54, 100)

print(f'\nRECEIPT 2')
print(f'------------------')
display_receipt(40, 40)

print(f'\nRECEIPT 3')
print(f'------------------')
display_receipt(45.43, 25)





