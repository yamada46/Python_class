#!/usr/bin/env python3
'''
Mod7_Lab2.py
This lab will scrape a website
'''
# import some packages and modules
import numpy as np
import requests
from bs4 import BeautifulSoup

# setup url as a string
url = "https://www.3tier.com/account/login/?next=/dashboard/"

# Now we can use urllib to pull down all the html and store it in a page variable:
response = requests.get(url)

# This gives us back a requests object that allows us to pull out different parts of the web page for parsing using beautifulsoup.
print(response.headers)
content = response.content

# Parsing Web Pages
# Now that we have pulled down all the html, let's convert it to beautifulsoup format so that we can read it:
soup = BeautifulSoup(content, "html.parser")

# We can use beautifulsoup's prettify function to print the html from our soup object in a more readable format so that we can figure out where to grab the states and capitals:
cities_a = soup.find_all("a", "List of cities in Canada")
print(soup.prettify())

# For example, if we wanted to grab out the information in a title tag:
print(soup.title)

# We can also automatically convert this to a string:
print(soup.title.string)
