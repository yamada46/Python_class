'''
ITFDN2018 Homework2
Create a script fo a customer purchasing a car and adding purchase price, sale tax, licensing fee, dealer prep fee. Calculate total cost and a database entry with unique ID, last neam area-code
Python3 code

'''

'''
Hello Christopher Robin! 

Thank you for your purchase of a Nissan Versa. Following is a break down of your total price: 

Sales Price: $2000.00

Tax: $50.00

Licensing Fee: $50.00

Dealer Prep Fee: $50.00

Total Price: $2150.00

You have been assigned an ID number of BIN_503. Please refer to this ID number if you have any questions 


'''

# Get the purchaser name
purchaser_name = input("What is your first, middle and last name? Please separate your names with commas. \n")
#print(purchaser_name)

fullname = purchaser_name.split(",")
#print(fullname[2])
last_name = fullname[2]
last_name_len = len(last_name)
#print(last_name_len)
last_four = last_name[last_name_len - 4:last_name_len]
#print(last_four)

# Get purchaser address
purchaser_address = input("Enter your address \n")
#print(purchaser_address)

# Get purchaser phone number
purchaser_phone = input("Enter your phone number, including area code xxx-xxx-xxxx \n")
#print(purchaser_phone)

phone_number = purchaser_phone.split("-")
#print(phone_number[2])

# Enter the type of car purchased
type_of_car = ("Enter your Make and Model of car: \n")
#print(type_of_car)

# Enter price of car purchase
base_price = input("Enter Base Price =  \n$ " )
base_decimal = float(base_price)
#print(base_decimal)

# Enter sales tax
sales_tax_rate = input("Enter Seattle car sales tax rate: \n")
num_places = len(sales_tax_rate)
#print(num_places)

if "%" in sales_tax_rate:
    num_places = int(num_places) - 1
    print(num_places)
    percent = sales_tax_rate[0:3]
    print(percent)
    sales_tax_decimal = float(percent) / 100
#    print(sales_tax_decimal)

else:
    sales_tax_decimal = float(sales_tax_rate) / 100
#    print(sales_tax_rate)

total_sales_tax = base_decimal * sales_tax_decimal
#print(total_sales_tax)

# Enter the dealer's prep fee
prep_fee = input("Enter the dealer's preparation fee: \n$ ")
prep_fee_decimal = float(prep_fee)
#print(prep_fee_decimal)

# Enter the licensing fee
lic_fee = input("Enter the licensing fee: \n$ ")
lic_fee_decimal = float(lic_fee)
#print(lic_fee_decimal)

total_sales = base_decimal + total_sales_tax + prep_fee_decimal + lic_fee_decimal

purchaserID = last_four + "_" + phone_number[2]
#print(purchaserID)

print("Hello",fullname[0], fullname[1], fullname[2],",\n")

print("Thank you for your purchase of the ", type_of_car,". Here is the final totals for your purchase.\n" )

print("Sales Price: $",base_decimal,"\n")

print("Sales Tax: $", total_sales_tax,"\n")

print("Licensing Fee: $", lic_fee,"\n")

print("Dealer Prep Fee: $", prep_fee,"\n")

print("Total price = $", total_sales,". For any questions, your reference number is: ", purchaserID,sep="")

'''
I could not make the float numbers show 2 decimal places. And I tried to make a CalculateTaxes function, but I deleted it because \
I couldn't get it to work.
'''



