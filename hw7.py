'''
hw7.py
This script will scrape a website from user input, use Beautiful Soup to
parse and return all the tags from user input, use the tag.text property,
open an appendable file and write to the file, create a main function

Homework requirements:
Create a function that allows you to pull out a tag (passed as an argument to your function) from any URL (also passed as an argument to your function)
Create a function to format the output in a meaningful way
Create a function to write the formatted results to a txt file
Create a main function that allows the script to be run on its own from the command line
Upload your script and output file to canvas for full credit
'''
#

# import requests (a library) and bs4 (BeautifulSoup4)
import requests
import bs4

# make a function to define main
#def main():      # does stuff at the command line



def find_tags(url, tag):
    response = requests.get(url)
    dom = bs4.BeautifulSoup(response.content, "html.parser")
    return dom.find_all(tag)

def tag_text(tags):
    tag_list = []
    for tag in tags:
        tag_list.append(tag.text)
    return tag_list

def find_attrbs(tags):
    tag_attrbs = []
    for tag in tags:
        tag_attrbs.append(tag.attr)
    return tag_attrbs

def write_text(tags_list):
    file = open("/Users/gailyamada/PycharmProjects/ITFDN2018/tag.txt", "a")
    for tag in tags_list:
        file.write(tag + '\n')

# get an input for a url as a string and print it out
url = input("Enter a URL you would like to scrape data from: \n")
print("The URL you have chosen is: {}.".format(url))

# get an input for a tag to find
tag = input("What tag would you like to search for? \n")

print("The tag you have entered is: {}\n".format(tag))

# find the tags
tags = find_tags(url, tag)

# convert to text
tags_list = tag_text(tags)
print(tags_list)

# write to tag.txt
write_text(tags_list)

'''


# We can use beautifulsoup's prettify function to print the html from our soup object in a more readable format so that we can figure out where to grab the states and capitals:
print(soup.prettify())

# For example, if we wanted to grab out the information in a title tag:
soup.title

# We can also automatically convert this to a string:
title_cities = soup.title.string
print(title_cities)
#List of cities in Canada - Wikipedia


# If we want to view information contained in all tags, for example, h1, then we can use the findall method:

all_a = soup.find_all("a")
cities_a = soup.find_all("a", "List of cities in Canada")
#can_cities = soup.find_all("List of cities in Canada")
# This returns an iterable object that we can loop through with a for loop:
cities_canada = []
for x in all_a:
    print(x)



# To further refine the information we're looking for, we can add a class argument to find_all() that allows us to search within div tags:

cities_a_wiki = soup.find_all("a", "List of cities in Canada")
print(cities_a_wiki)
for x in all_a_wiki:
    print(x)

# We can also index this item just like a list:
all_a_https[0]


<a class="https" href="https://www.packtpub.com/application-development/python-gui-programming-cookbook-second-edition">Python GUI Programming Cookbook - Second Edition</a>

# We can also loop through other the metadata (attributes, just like variables) that are nested inside of the dev tag that we pulled out:

for x in all_a_https:
    print(x.attrs['href'])

# We can now use this information to create a dictionary of books and their related links:

data = {}
for a in all_a_https:
    title = a.string.strip()
    data[title] = a.attrs['href']

# BONUS: Now that you've worked through this tutorial, try to parse data from another web site, and paste your code here for credit.

Here's a great walk-through on web scraping with beautifulsoup:

http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.htm
'''

'''
hw7.py

Create a function that allows you to pull out a tag (passed as an argument to your function) from any URL (also passed as an argument to your function)
Create a function to format the output in a meaningful way
Create a function to write the formatted results to a txt file
Create a main function that allows the script to be run on its own from the command line
Upload your script and output file to canvas for full credit
Example of what running the first function should look like for the end-user:
get_div(url="https://en.wikipedia.org/wiki/List_of_cities_in_Canada", (Links to an external site.)Links to an external site. tag="a")
Denise created a Github repository for Immer barley data that has an easily digestible html structure: https://denisemauldin.github.io/immer/index.html (Links to an external site.)Links to an external site.
Stretch goal:
Use the tutorial here (Links to an external site.)Links to an external site. to learn about lxml, tree, and Xpath.  Create Xpaths for the Immer barley data to create a list of the varieties and a dictionary of the barley data.  Be careful that you're getting only the data!

'''