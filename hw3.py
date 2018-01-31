'''
hw3.py


Create a script called hw3.py
Ask the user to enter a starting and ending number

Ask the user to enter a starting and ending number
The user must not enter a starting number less than 1
The user must enter an ending number at least 5 times greater than the starting number
Create checks and error messages for the above
Create a list of integers in the range of the user's starting and ending numbers
Print out the number and index of each item in the list that is even
Sum all the odd numbers in the list using a for loop ( hint: append odd numbers to a list and then sum() that list )
Print out the cumulative sum calculated above
 Upload your python file to Canvas.
'''

print("In this exercise the user will enter a low and high number\n")

# Input low number, integer < 1
lower_number = int(input("Please enter the low integer number greater than 1: \n"))

while lower_number <= 1:
    lower_number = int(input("The number must be an integer and greater than 1! Enter a low number: \n"))
#    print(lower_number)

# Input higher number, must be at 5 times as big as lower number

higher_number = int(input("Please enter an integer at least 5 times larger than the low number: \n"))
while higher_number <= lower_number * 5:
    higher_number = int(input("The higher number must be at least 5 times as large as the low number! Enter another higher number: \n"))
# print(lower_number, higher_number)

# Create a list using the input for the lower and higher value
all_numbers = list(range(lower_number, higher_number))
# print(all_numbers)

# Set up a list to store the odd numbers
odd_numbers = []

# Make a list and index for the even numbers and print out
print("\nThis is the list and index for the even numbers:")
for x, number in enumerate(all_numbers):
    if number % 2 == 0:
        print("\n{} is at index {}".format(str(number), str(x)))
       
    else:
        odd_numbers.append(number)

# Get the sum off the odd numbers and print it out
odd_sum = (sum(odd_numbers))

print("\nThe sum of the odd numbers is:", odd_sum, "\n")



