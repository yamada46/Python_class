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
residence = "{city} {state} {country}".format(city=user_city.title(), state=user_state.title(), country=user_country.title())

print(residence);

# Ask how many and what are the colors in their country flag


# if want to use a loop
# numcolor_flag = input("How many colors are in your country's flag? " )
#    for i = 0, i<numcolor_flag, i++
flag_colors = input("What are the colors of your country flag? Please separate the colors by commas. \n")
# If don't want to use a loop


#user_input_colors = flag_colors.split(',')
#print(len(flag_colors));
print(flag_colors);
#len(flag_colors);

# Put all of the info in a sentence
#print("Your name is ",user_name" and you are from "user_residence", your country flag has the colors ",flag_colors".");
#print("Your name is ",user_firstname,' ',user_lastname'.' "You are from" user_city.title',')
print("Your name is "user_name);
