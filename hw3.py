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
Example Output:
Please enter a starting number: 2

Please enter an ending number: 200

Even numbers in your list:

2 is at the 3rd index

4 is at the 5th index...

The sum of your number list is: 500 (I made that number up)
'''

print("User will enter a low and high number")

lower_number = int(input("Please enter an integer greater than 1: "))
while lower_number <= int(1):
    print("The number must be an integer and greater than 1 ")
else:
    print(lower_number)


