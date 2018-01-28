'''
Mod3_Lab2

make a variable with one animal
find unique letter
give user letters + 3 guesses
compare each guess to unique letters
print out the matches
'''
# Make a list of animal
animal = "raccoon"
unique = set(animal)
print(unique)

# store guesses
guessed_letter = set()
num_guess = len(unique)
print(num_guess)
print("Figure out the secret animal. Guess some letters in it's name! You get ", num_guess," tries ")

# get user input

counter = 0
while counter < num_guess:
    guess = input("Guess a letter in the secret animal's name: ")
    if guess in unique:
        print("Yes, you guessed a letter! ")
        guessed_letter.add(guess)
        print(guessed_letter)
        counter+= 1
    else:
        print("That letter is not in the animal name")
        counter+= 1

print("These are the letters you have guessed correctly ", guessed_letter)
print("The number of letter in the secret animal name is ",len(animal))
guess_animal = input("Guess what the animal is: ")
if guess_animal == animal:
    print("Congrat! You've guessed correctly!")
else:
    print("Sorry you lose!")
