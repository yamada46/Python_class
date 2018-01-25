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

# Get the purchaser name
purchaser_name = input("What is your first, middle and last name? Please separate your names with commas. \n")
print(purchaser_name)

fullname = purchaser_name.split(",")
print(fullname[2])
last_name = fullname[2]
last_name_len = len(last_name)
print(last_name_len)
last_four = last_name[last_name_len - 4:last_name_len]
print(last_four)

# Get purchaser address
purchaser_address = input("Enter your address \n")
print(purchaser_address)

# Get purchaser phone number
purchaser_phone = input("Enter your phone number, including area code xxx-xxx-xxxx \n")
print(purchaser_phone)

phone_number = purchaser_phone.split("-")
print(phone_number[2])

# Enter the type of car purchased
type_of_car = "Subaru CrossTrek"
print(type_of_car)

# Enter price of car purchase
base_price = input("Enter Base Price =  \n$ " )
base_decimal = float(base_price)
print(base_decimal)


# Enter sales tax
sales_tax_rate = input("Enter Seattle car sales tax rate: \n")
num_places = len(sales_tax_rate)
print(num_places)

if "%" in sales_tax_rate:
    num_places = int(num_places) - 1
    print(num_places)
    percent = sales_tax_rate[0:3]
    print(percent)
    sales_tax_decimal = float(percent) / 100
    print(sales_tax_decimal)

else:
    sales_tax_rate = float(sales_tax_rate) / 100
    print(sales_tax_rate)

total_sales_tax = base_decimal * sales_tax_decimal
print(total_sales_tax)

# Enter the dealer's prep fee
prep_fee = input("Enter the dealer's preparation fee: \n$ ")
print(prep_fee)

purchaserID = last_four + "_" + phone_number[2]
print(purchaserID)



