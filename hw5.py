#! /Users/gailyamada/PycharmProjects/ITFDN2018/venv/bin/python3
'''

From the previous lab:

Browse to a free copy of "The Land That Time Forgot" (Links to an external site.)Links to an external site. (or a different book)
Right-click on your browser
Select "save as"
Save as a .txt file
Read in the file and store in a list
Convert the list of book lines into a list of the words (hint: use a for loop and list.extend)
For this homework:

Print a sentence using format with the total number of words and the unique number of words (hint: use a set)
Calculate the word (Links to an external site.)Links to an external site. frequency (Links to an external site.)Links to an external site. using the word list, the word set, and a for loop with list.count (Links to an external site.)Links to an external site. and store it in a dictionary (hint: don't forget to use float)
Calculate the word with the maximum frequency (hint: use max (Links to an external site.)Links to an external site.)
Get the minimum frequency (hint: use values (Links to an external site.)Links to an external site.)
Store all of the words that have the minimum frequency in a list (hint: use a for loop and items (Links to an external site.)Links to an external site.)
Print a sentence of the minimum frequency and the number of words with that frequency
Print a sentence of the percentage of words that are unique in the book (hint: use :.1f in your format)
'''
# from Mod5_Lab2
# import a sort operator
import operator
# sortedList =sorted(h.items(), key=operator.itemgetter(1,0) , reverse=True)

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

# Convert list of lines into a list of lines of words, then list of words only
words = []
words2 = []
words3 = []

for line in list_file:
    line = line.strip()
    line = line.lower()
    line = line.replace(",", "")
    line = line.replace(".", "")
    line = line.replace(" '", " ")
    line = line.replace("' ", " ")
    line_list = line.split(" ")
    words.append(line_list)    # chunks of words concatenated together
    words2.extend(line_list)   # just the words by themselves
#print(words2[0:10])

# print how many words are in the file
print("The File has {} many words.\n".format(len(words2)))

#print(words[0:5])
#print(words2[0:5])


# how many words are in the file
num_words = len(words2)
#print(num_words)

# get number of unique words
unique_set = set(words2)
num_unique = len(unique_set)
#print(num_unique)

# Print a sentence using format with the total number of words and the unique number of words (hint: use a set)
print("The total number of words in the 'land_time_forgot.txt is {} and the number of unique words is {}.\n".format(num_words, num_unique) )

# get the frequency of each word
# Calculate the word frequency using the word list, the word set, and a for loop with list.count and store it in a dictionary (hint: don't forget to use float)

word_dict = {}
for word in words2:
    if word in word_dict.keys():
        word_dict[word] = word_dict[word] + 1
    else:
        word_dict[word] = 1
#print(word_dict)
#print(word_dict["the"])

# use the import operator to sort the dictionary by ascending counts of words
# I just googled this because I wanted to sort the dictionary descending (I don't understand it tho, but it worked)
sortedDict =sorted(word_dict.items(), key=operator.itemgetter(1,0) , reverse=True)
#print(sortedDict)

# get the word that is used the most and the least
max_word = max(word_dict, key=word_dict.get)    # gets the word with the maximum times used
min_word_count = min(word_dict, key=word_dict.get)    # gets the value that is lowest which would be 1
#print(max_word)
#print(min_word_count)      # I thought this should say 1 but it says 'title:'


'''
#couldn't get this to work
# get the list of words used once

words_once = []
for word in word_dict.items():
    if word == 1:
        words_once = words_once.append(word)
print(words_once)
'''

# print out a sentence giving the word used the most and the list of miminum words
print("The word used the most in this text is '{}' which is used {} times.".format(max_word, word_dict["the"]))

#print("The list of words only used once is {}.".format(min_words)

# figure out the percentage of unique words to total words
unique_percent = float(num_unique/num_words) * 100
#print(unique_percent)


# Print a sentence of the percentage of words that are unique in the book (hint: use :.1f in your format)
print("The percentage of words that are unique in this text is {:.1f}% \n".format(unique_percent))

