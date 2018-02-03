#! /Users/gailyamada/PycharmProjects/ITFDN2018/venv/bin/python3
'''
hw4.py

Assignment 04 Overview
Define two lists at the top of your file (you can make them anything, feel free to be creative), such as the ones below:

names = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank",
    "Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]
These lists should match up, so Alice’s age is 20, Bob’s age is 21, and so on.

Use the zip function to merge these lists into a dictionary. (What data type does zip() return? How do you coerce that to the right data type?)
The names should be the keys, and the age should be the value.
Ask the user to input a user name
Use a while loop to keep asking the user to input a user until they find someone in the dictionary, give them up to five tries by using a counter outside the while loop
Return the user's age, as shown below
Your program should print out the response, as follows:

"Please input an user to find out their age: "
"Alice"
"Alice is 57!"

"Tabitha"
"There is nobody here named Tabitha, please try again: "


'''
# Create two lists
hair_colors = ["black", "light brown", "med brown", "dark brown", "light blond", "blond" , "auburn", "red", "gray", "white"]
people = ["Sheree", "Henry", "Jim", "Kim", "Verene", "Lynda", "Jen", "Terry", "Iky", "Gabi"]
print(hair_colors, people)

# Combine the two lists into a dictionary
hair_tuple_people = list(zip(hair_colors, people))

hair_people_dict = dict(hair_tuple_people)

# Print out dictionary
print(hair_people_dict)

for key, val in hair_people_dict.items():
    print(key, val)


"Please input an user to find out their age: "
"Alice"
"Alice is 57!"

"Tabitha"
"There is nobody here named Tabitha, please try again: "
