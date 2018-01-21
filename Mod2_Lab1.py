'''
Mod2_Lab1
Create variables to store user input for:
User name
User phone number
Favorite cheese
Average monthly amount spent on their favorite cheese
Calculate the daily amount this user spends on cheese and store this value as a variable
Use the string split() method to store the last four digits of the user's phone number as a variable
Use the string slicing method to store the first three letters of the user's name as a variable
Combine the phone number and username variables to create an account ID
Use the replace() method to replace the first letter of your User ID with a Z and store that value as the final user ID
Print out a string telling the user what their account ID is, and letting them know what their daily cheese spending habits look like.
Feel free to add as much snark as you want.
Make sure your script runs, and upload the python script here.

'''

# Input user name
userName = input("What is your name? \n")
print(userName)

# Input user phone number
userPhone = input("What is your phone number? \n")
print(userPhone)

# Input user favorite cheese
favCheese = input("What is your favorite cheese? \n")
print(favCheese)


# Input average $$ spent on cheese
amtPerMonth = input("How much do you spend on cheese per month? $")
float(amtPerMonth)
print(amtPerMonth)

# Calculate daily cheese spending rate for dec
dailyCheeseExpense = (float(amtPerMonth) / 31)
print(dailyCheeseExpense)
