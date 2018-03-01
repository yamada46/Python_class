'''
The comments down at the bottom are what ran just fine before I added the 'def main()'
I don't understand what making it work at the command line means

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

# make a function to define main - don't really understand - does stuff at command line
def main():
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
#    print(tags_list)

# write to tag.txt
    write_text(tags_list)

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

if __name__=="__main__":
    main()

'''
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
