'''
Mod6Lab1.py

For this lab:

Create a main section at the bottom of the code
Update the code to have a function that reads in the file and returns contents as a list
Update the code to have a function that converts the list of book lines into a list of the words
Update the main section to call the function that reads the file and the function that converts the book lines into a list.  Remember to pass the appropriate variable into the function and return the value you want and store it in a variable
Update the main section to create a word set and print the sentence about unique words
Update the code to have a function that calculates the word count by taking in the word list and return the dictionary
Update the main section to call the function that calculates the word count and find the word with the maximum count (hint: use max)
Update the code to have a function that calculates the minum word frequency and gets the list of words from the word frequency dictionary
Update the main section to call the minimum word function and print the results
Post your solution to the discussion board.
'''
'''
def reader(text_name, file_name)
with open("./test_name") as file_name:
    with open("./land_time_forgot.txt") as file:
    lines = file.readlines()

def word_list = []
    for line in lines:
    word_list.extend(line.split(" "))

    word_set = set(word_list)
    print("There are {} words in the book and {} of them are unique".format(
        len(word_list), len(word_set)))

    word_freq = {}
    for word in word_list:
        if word in word_freq:
            word_freq[word] = word_freq[word] + 1
        else:
            word_freq[word] = 1

    max_word = max(word_freq, key=word_freq.get)

    print("Most frequent word is '{}' at {} with frequency {}".format(
        max_word, word_counts[max_word], word_freq[max_word]))

    min_word_freq = min(word_freq.values())
    min_words = []
    for word, fr in word_freq.items():
        if fr == min_word_freq:
            min_words.append(word)

    print("The lowest word_frequency is {} and there are {} words in the book with that word_frequency".format(min_word_freq, len(min_words)))lines = file.readlines()

    word_list = []
    for line in lines:
    word_list.extend(line.split(" "))

    word_set = set(word_list)
    print("There are {} words in the book and {} of them are unique".format(
        len(word_list), len(word_set)))

    word_freq = {}
    for word in word_list:
        if word in word_freq:
            word_freq[word] = word_freq[word] + 1
        else:
            word_freq[word] = 1

    max_word = max(word_freq, key=word_freq.get)

    print("Most frequent word is '{}' at {} with frequency {}".format(
        max_word, word_counts[max_word], word_freq[max_word]))

    min_word_freq = min(word_freq.values())
    min_words = []
    for word, fr in word_freq.items():
        if fr == min_word_freq:
            min_words.append(word)

    print("The lowest word_frequency is {} and there are {} words in the book with that word_frequency".format(min_word_freq, len(min_words)))
'''
------------------
if __name__ == "__main__":
    pass
'''
my old hw5.py
# import a sort operator
import operator
# sortedList =sorted(h.items(), key=operator.itemgetter(1,0) , reverse=True)

# open the file
def read_text(file_name)
    with open(file_name) as text:
        list_file = text.readlines()
    return(list_file)
    
    
lines = list_file
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
#words3 = []

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
min_word_count = min(word_dict.values())    # gets the value that is lowest which would be 1
#print(max_word)
#print(min_word_count)      # I thought this should say 1 but it says 'title:'


# get the list of words used once
words_once = []
for word, times in word_dict.items():
    if times == min_word_count:
        words_once.append(word)
#print(words_once)

# get the number of words used once
num_words_once = len(words_once)
#print(num_words_once)


# print out a sentence giving the word used the most and the list of miminum words
print("The most repeated word in this text is '{}' which is used {} times.".format(max_word, word_dict["the"]))
print("There are {} words with a minimum count of 1 \n".format(num_words_once))

#print("The list of words only used once is {}.".format(min_words)

# figure out the percentage of unique words to total words
unique_percent = float(num_unique/num_words) * 100
#print(unique_percent)

# Print a sentence of the percentage of words that are unique in the book (hint: use :.1f in your format)
print("The percentage of words that are unique in this text is {:.1f}% \n".format(unique_percent))







'''