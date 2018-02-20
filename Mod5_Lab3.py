#! /Users/gailyamada/PycharmProjects/ITFDN2018/venv/bin/python3
'''
Module 5 - Lab 3
Denise Elizabeth Mauldin

Let's do some analysis of the Seattle Wage Data CSV file

Make sure you have downloaded the data from here:

https://catalog.data.gov/dataset/city-of-seattle-wage-data/resource/1b351da9-d1a9-48e4-850c-a1af51c43852 (Links to an external site.)Links to an external site.
with open
For this lab:
Read in the CSV file using csv.reader
Store the header line in a variable using next (Links to an external site.)Links to an external site.
Create a dictionary to store the list of 'Hourly Rate' by job title (hint: this is a dictionary where the value is a list - seattle[job] = [rates].  You'll need to use dictionary.get to see if the key exists in each dictionary and create it if it does not.)
Write the dictionary to a file
Stretch Goals

After your data structure is created, use a for loop to go over each job and calculate the average pay
Print a sentence for each job saying how many people work that job and what the average pay is. (hint: if there's one person, you just need to print the first value of the rates list)


Calculate the highest paying job
Print the seattle dictionary to a file
Store the department as the first key and print out the average wage by job title in the department

'''
# open the file and read in the file
import csv
file_handle = open("./City_of_Seattle_Wage_Data.csv")
reader = csv.reader(file_handle)

for row in reader:
    print(row)

'''
header = []
header = row[0].split(",")
print(header)

# get the header line and save it as header
#header = row[0].split(",")

'''

