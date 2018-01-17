# Create a script that asks user for 3 inputs, combine inputs in a sentence string, then print sentence
# Ask user input last name, first name, middle name

user_lastname = input("What is your last name? \n")
user_firstname = input("What is your first name? \n")

user_name = "{first} {last}".format(first=user_firstname.title(), last=user_lastname.title())
print(user_name);

# Ask what city and country user is from

user_country = input("What country are you from? \n")
user_state = input("What state are you from? \n")
user_city = input("What city are you from? \n")

user_residence = "{country} {state} {city}".format(country = user_country.title(), state = user_state.title(), \
                                                   city = user_city.title())
print(user_residence);

# Ask how many and what are the colors in their country flag

# if want to use a loop
# get number of flag colors
# numcolor_flag = input("How many colors are in your country's flag? " )


#    for i = 0, i<numcolor_flag, i++

# If don't want to use a loop
flag_colors = input("What are the colors of your country flag? Please separate the colors by commas. \n")
color_list = flag_colors.split(',')

print(color_list);
print(flag_colors);
print("Your name is ", user_name)


#print("Your name is ", user_name", and you are from ", user_residence".");
