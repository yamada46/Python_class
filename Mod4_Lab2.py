'''
Module 4 - Lab 2

Dictionaries are great data structures to use for grouping and counting information. For this lab, we're going to create a list of names to group by length, and then count how many names occur in each group.

Create the following name list and add in at least five female names (with repeats) to support women in tech!
names = ['mark', 'henry', 'matthew', 'paul', 'robert', 'joseph', 'carl',
 'luke', 'robert', 'joseph', 'carl', 'michael', 'mark', 'henry', 'matthew']
Create an empty dictionary to store your values
Create a for loop that iterates through the names to add each one to the dictionary along with a count
Hint: See the lecture on Counting with Dictionaries
'''
# Module 4 - Lab 2

# Create the following name list and add in at least five female names (with repeats) to support women in tech!
names = ['mark', 'henry', 'matthew', 'paul', 'robert', 'joseph', 'carl',
 'luke', 'robert', 'joseph', 'carl', 'michael', 'mark', 'henry', 'matthew']

fem_names = ['layla','jen','louise','kim','halley','louise','kim']

full_names = names + fem_names

# Create an empty dictionary
dict_names = {}

# Create a for loop that iterates through the names to add each one to the dictionary along with a count
for name in full_names:
    if name in dict_names:
        dict_names[name] = dict_names[name] + 1
    else:
        dict_names[name] = 1

print(dict_names)

