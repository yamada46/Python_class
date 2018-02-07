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
people = ["Sheree", "Henry", "Helen", "Kim", "Verene", "Lynda", "Jen", "Terry", "Iky", "Gabi"]
hair_colors = ["black", "light brown, green", "med brown, blue, purple", "dark brown", "light blond, pink", "blond" , "auburn", "red", "gray, white, black", "white"]
# print(people, hair_colors)

# Or combine the two list with the key being the people's name instead of hair color
people_tuple_hair = list(zip(people, hair_colors))

people_hair_dict = dict(people_tuple_hair)
# people_hair_dict

# Get some names guesses from the user
print("\nTry to guess a name on the list to see their hair color(s)! \n")

count = 0
wrong_guess = []
while count < 5:
    print("You have", 5 - count, "guesses. \n")
    guess = input("Guess a name in the list: \n")
    if guess in people_hair_dict:
        print("\nYes! {} is a name in the list and has hair color of {}. \n".format(guess, people_hair_dict[guess]))
#        print(guess)
    else:
        print("\n{} is not one of the names in the list. Guess again: \n".format(guess))
        wrong_guess.append(guess)
    count += 1

if count == 5:
    print("You have one guess left: \n")
print("These are all the wrong guesses!\n\n", list(wrong_guess))
'''     
    else:
        print(guess, " is not in the list. Guess another name: \n)"
#        count += 1
'''
