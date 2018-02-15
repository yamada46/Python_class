#! /Users/gailyamada/PycharmProjects/ITFDN2018/venv/bin/python3

'''
Mod5_Lab2
Convert the list of book lines into a list of the words (hint: use a for loop and list.extend (Links to an external site.)Links to an external site. OR two for loops and list.append)
Print a sentence using format with the total number of words
Use split to get the project_title and author from the first line
The first line of the book is: Project Gutenberg's The Land That Time Forgot, by Edgar Rice Burroughs
project_title is : Project Gutenberg's The Land That Time Forgot
author is : Edgar Rice Burroughs
Use split to get the project and title from project_title (hint: use split and then add the word back to the appropriate variable)
project is : Project Gutenberg's
title is : The Land That Time Forgot
Print the author, then the title, followed by the project using format.
Post your solution to this discussion board

'''

# open the file
with open("./land_time_forgot.txt") as file:

# read file into a list of lines
    list_file = file.readlines()

# get number of lines
num_lines = len(list_file)

# get first line
first_line = list_file[0]
print(first_line)

# get the author, project_title
project_title_author = first_line.split(", by ")
print(project_title_author)
print("The project title is '{}' by {}".format(project_title_author[0], project_title_author[1]))

# Convert list of lines into a list of words
words = []
for line in list_file:
    line = line.strip()
    line_list = line.split(" ")
    words.append(line_list)
#print(words)

# print how many words are in the file
print("The File has {} many words.\n".format(len(words)))


