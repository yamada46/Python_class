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
    num = num_slices/slices_per_pizza
    if num_slices % slices_per_pizza == 0:
        return num
    else:
        return int(num) + 1

'''
pizzas_price function multiplies number of pizzas * per pizza price ($10)
'''
def pizzas_price(pizzas_needed, cost_per_pizza):
    price = pizzas_needed * cost_per_pizza
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
total_tax_tip_fee function determines the total bill including delivery charge
'''
def total_tax_tip_fee(pizzas_cost, sales_tax_pizzas, tip_amt, delivery_cost):
    totals = float(pizzas_cost + sales_tax_pizzas + tip_amt + delivery_cost)
    return totals
'''
cost per person is the cost of pizzas with tax, tip, delivery fee divided by number of people
'''
def cost_per_person(grand_total, num_people):
    cost_each = grand_total/num_people
    return cost_each

# Get the input for people's names and number of pizza slices they'd like to eat
print("Who wants pizza? The large pizza has 8 slices. And there are 8 of us. \n")

people_slices = []
name_list = ["Sheree", "Melissa", "Zack", "Karen", "JoAnn", "Elisha", "Lisa", "Gail"]
for name in name_list:
    slices = input("{}, how many slices do you want? ".format(name))
    people_slices.append(int(slices))
#print(people_slices)

# enter cost per pizza, slices per pizza, 9.6% sales tax, 15% tip, delivery fee
cost_per_pizza = float(10.00)
slices_per_pizza = int(8)
percent_tax = float(9.6)
percent_tip = float(15)
delivery_cost = float(3.99)

# Find out the average slices per person
num_slices = sum(people_slices)
num_people = len(people_slices)

avg = avg_slices(num_slices, num_people)

# find out the number of slices of pizza needed for everyone
num_slices = sum(people_slices)

# find out the number of pizzas needed
pizzas_needed = num_pizza(num_slices)


# find out the total cost for just the pizzas
pizzas_cost = pizzas_price(pizzas_needed, cost_per_pizza)
#print(pizzas_cost)

# find out the sales tax for the pizzas
sales_tax_pizzas = sales_tax(pizzas_cost, percent_tax)
print(sales_tax_pizzas)
total_price = float(pizzas_cost + sales_tax_pizzas)
#print(total_price)

# find out the tip for the pizzas total cost with tax
tip_amt = tip_amount(total_price, percent_tip)

# find out the total cost for the pizzas with tax, and delivery fee
grand_total = total_tax_tip_fee(pizzas_cost, sales_tax_pizzas, tip_amt, delivery_cost)

# find out the cost per person
each_cost_8_people = cost_per_person(grand_total, num_people)

# print out the total slices, how many pizzas, grand_total, average number of slices per person
print("The total number of slices is {} for everyone, which is at least {} pizzas.\n ".format(num_slices, pizzas_needed))
print("The grand total including tax, tip, delivery fee is ${:.2f} ".format(grand_total))
print("The {:.1f} is the average number of slices per person. So the cost per person is ${:.2f} \n".format(avg, each_cost_8_people))





