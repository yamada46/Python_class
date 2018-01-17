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

# Ask how many and what are the colors in their country flag

# if want to use a loop
# numcolor_flag = input("How many colors are in your country's flag? " )
#    for i = 0, i<numcolor_flag, i++

# If don't want to use a loop
flag_colors = input("What are the colors of your country flag? Please separate the colors by commas. \n")

user_input_colors = flag_colors.split(',')

# Put all of the info in a sentence
#print("Your name is ",user_firstname.title,' ',user_lastname.title'.' "You are from" user_city.title',')
#print("Your name is ",user_firstname,' ',user_lastname'.' "You are from" user_city.title',')
print(user_firstname, userlastname)
