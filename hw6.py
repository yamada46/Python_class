#! /Users/gailyamada/PycharmProjects/ITFDN2018/venv/bin/python3

'''
hw6.py
This python script will calculate the cost of pizza for movie night.

Get user input for the following:
Number of people who want pizza
Average number of slices per person
You can store these as a single integer, or use a dictionary to map names to values, up to you
Create the following static (unchanging) variables:
Pizza cost = $10.00
Total slices = 8
Tax rate of 9.6%
Tip rate of 5 -15%
Delivery fee of $3.99
Write functions to:
Calculate how many pizzas to order based on number of people and average slices
Total pizza cost
Cost per person
Stretch goals:

Add an option to calculate the tip by person or by slice.
Update your pizza script to read in a file (txt or csv) of how many slices of pizza different people want (ex: Daniel, 3) and calculate the cost for each person individually.
How many slices are leftover?
Example Output:


You need 6 pizzas
The total cost is $78.90

Each person owed $5.26

'''
# Get the input for people's names and number of pizza slices they'd like to eat
name_list = ["Sheree", "Melissa", "Zack", "Karen", "JoAnn", "Elisha", "Lisa", "Gail"]

people_slices = [2, 3, 4, 3, 3, 2, 2, 2]

# Put the unchanging variables in a tuple
pizza_tuple = (10.00, 8, 9.6, 15, 3.99)

'''
Good practice to give notes to functions
'''
'''
total_slices function sums up all of the slices of pizza people want
'''
def total_slices():
    slices = sum(people_slices)
    return slices

'''
num_pizza function determines how many pizzas need to be ordered 
'''
def num_pizza(num_slices):
    num = num_slices/pizza_tuple[1]
    if num_slices % pizza_tuple[1] == 0:
        return num
    else:
        return int(num) + 1

'''
pizzas_price function multiplies number of pizzas * per pizza price ($10)
'''
def pizzas_price(num_pizzas, per_pizza_price):
    price = num_pizzas * per_pizza_price
    return price

'''
sales_tax function determines the total sales tax on the pizza order (9.6%)
'''
def sales_tax(total_price, percent_tax):
    tax = percent_tax * total_price/100
    return tax

'''
tip_amount function determines the amount of tip to add (5-20%)
'''
def tip_amount(total_price, tip_percent):
    tip = total_price * tip_percent/100
    return tip

'''
avg_slices function determines the average amount of pizza slices per person
'''
def avg_slices(num_slices, num_people):
    avg = num_slices/num_people
    return avg

'''
total_tax_tip function determines the total bill including delivery charge
'''
def total_tax_tip(total_price, tax, tip, delivery_fee ):
    totals = float(total_price + tax + tip + delivery_fee)
    return totals

# Get the input for people's names and number of pizza slices they'd like to eat
print("Who wants pizza? The large pizza has 8 slices. \n")

people_slices = []
name_list = ["Sheree", "Melissa", "Zack", "Karen", "JoAnn", "Elisha", "Lisa", "Gail"]
for name in name_list:
    slices = input("How many slices do you want? ")
    people_slices.append(int(slices))
print(people_slices)

# Find out the average slices per person
num_slices = sum(people_slices)
num_people = len(people_slices)

avg = avg_slices(num_slices, num_people)

print("The average number of slices per person is {}.\n".format(avg))





