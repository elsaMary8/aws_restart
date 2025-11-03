import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)

isGuessedRight = False

while isGuessedRight != True:
    guess = input("Guess a number between 1 and 10:")
    if int(guess) == number:
        print("You guessed {}. Hurrayyy Correct!!!".format(guess))
        isGuessedRight = True
    else:
        print("You guessed {}.Sorry!!!Try again.".format(guess))