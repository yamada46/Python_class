'''
ITFDN2018 Homework2
Create a script fo a customer purchasing a car and adding purchase price, sale tax, licensing fee, dealer prep fee. Calculate total cost and a database entry with unique ID, last neam area-code
Python3 code

'''

'''
Gather the following user input and store each item as a variable: 
Purchaser name
Purchaser address
Purchaser phone number (entered as 503-555-1211)
Car Make/Model
Purchase Price
After the user inputs the above information, your program should add the following values to the sale price: 
Sales tax as a percent of sale price 
Licensing fee
Dealer prep fee
Calculate total cost (as a float)
Assign the car a unique ID composed of the last four letters of the purchaser's last name and their area code, separated by an underscore
Print out the information to the screen, with the same line breaks as shown in the example below
Make sure your script runs and submit it to canvas as a .py file. 
'''
'''
# Get the purchaser name
purchaser_name = input("What is your first, middle and last name? Please separate your names with commas. \n")
print(purchaser_name)

fullname = purchaser_name.split(",")
print(fullname)

# Get purchaser address
purchaser_address = input("Enter your address \n")
print(purchaser_address)
'''
# Get purchaser phone number
purchaser_phone = input("Enter your phone number, including area code xxx-xxx-xxxx \n")
print(purchaser_phone)

phone_number = purchaser_phone.split("-")
print(phone_number[3])

# Enter the type of car purchased
type_of_car = "Subaru CrossTrek"
print(type_of_car)


'''

# Enter price of car purchase
base_price = input("Base Price = (exact price including cents, no commas) " )
#dollars, cents = base_price.split(".")
print(base_price)

# see if there are 2 decimal places

# Calculate sales tax
sales_tax_rate = input("What is Seattle car sales tax rate? \n")
print(sales_tax_rate)
if sales_tax_rate == sales_tax_rate + "%"):
    sales_tax = float((sales_tax_rate - "%")/100)

else
    sales_tax = sales_tax_rate;
    

print(sales_tax)
'''