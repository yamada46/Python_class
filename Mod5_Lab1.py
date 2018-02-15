#! use python3
'''
Read the file into a list
Calculate the total number of lines in the file
Calculate the lines that are in 1/3rd of the file
Store the middle third of the book's lines in a list (hint: use list accessor methods)
Print the number of lines in the file and the number of lines in the middle third of the book
Print the line that is 1/3rd of the way through the book and the line that is 2/3 of the way through the book
Write to a file using write mode:  (hint: there should be 3 lines in the file when you're done)
The sentence about the line statistics
The two lines from the book
Post your solution to this discussion board

# Mod5_Lab1
'''
# open the file
f = open("./land_time_forgot.txt")
# creates a file handle


# read file into a list
list_file = f.readlines()
total_lines = len(list_file)

# print total lines
print(total_lines)

# Calculate the lines that are in 1/3rd of the file
third = int(total_lines /3)
print(third)

# slice out 1/3 way through line
line_third_way = list_file[third : third + 1]
print(line_third_way)

# slice middle third
middle_third = list_file[third : third * 2]
print(middle_third)

# slice out 2/3 line
line_two_thirds = list_file[third * 2 : (third * 2) + 1]

my_two_lines = str([line_third_way + line_two_thirds])


# write those 2 lines to a file
with open('output.txt', 'w+') as f:
    f.writelines(my_two_lines)
