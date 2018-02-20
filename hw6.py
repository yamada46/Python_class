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
'''
def open_file_as_list():
    with open("/Users/monster/PycharmProjects/intro_to_python/The_Land_That_Time_Forgot.txt") as file:
        lines = file.readlines()
        print(lines)

def lines_word_list():
    word_list = []
    for line in lines:
        word_list.extend(line.split(" "))
    print(word_list)

        word_set = set(word_list)
        print("There are {} words in the book and {} of them are unique.".format(len(word_list), len(word_set)))

    word_freq = {}
    for word in word_list:
        if word in word_freq:
            word_freq[word] = word_freq[word] + 1
        else:
            word_freq[word] = 1

    max_word = max(word_freq, key=word_freq.get)

    print("Most frequent word is '{}', with frequency {}".format(max_word, word_freq[max_word]))

    min_word_freq = min(word_freq.values())
    min_words = []
    for word, fr in word_freq.items():
        if fr == min_word_freq:
            min_words.append(word)

    print("The lowest word_frequency is {} and there are {} words in the book with that word_frequency".format(min_word_freq, len(min_words)))

def run_main():
    open_file = open_file_as_list()
    lines_into_words = lines_word_list()

    if __name__ == '__main__':


'''
name_list = ["Sheree", "Melissa", "Zack", "Karen", "JoAnn", "Elisha", "Lisa", "Gail"]

people_slices = [2, 3, 4, 3, 3, 2, 2, 2]

pizza_tuple = (10.00, 8, 9.6, 15, 3.99)

def total_slices():
    slices = sum(people_slices)
    return slices

def num_pizza(num_slices):
    num = num_slices/pizza_tuple[1]
    if num_slices % pizza_tuple[1] == 0:
        return num
    else:
        return int(num) + 1

def pizzas_price(num_pizzas):
    price = num_pizzas * pizza_tuple[0]
    return price

def sales_tax(total_price):
    tax = pizza_tuple[2] * total_price/100
    return tax

def tip_amount(total_price):
    tip = total_price * pizza_tuple[3]
    return tip

def avg_slices(slices,num_people):
    avg = slices/num_people
    return avg



num_slices = sum(people_slices)
num_people = len(people_slices)

avg = avg_slices(num_slices, num_people)

print(avg)




