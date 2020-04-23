from __future__ import print_function
import random


def guessing_game():
    print("Welcome")
    print("Choose your level")
    print("Level 1: Easy")
    print("Level 2: Medium")
    print("Level 3: Hard")
    level = int(input("Enter either 1, 2 or 3 for each corresponding level: "))

    if (level==1):
        print("Choose a number between 1-50 and you have 6 guesses: ")
        guess = 1
        while guess < 7:
            countdown = 6
            for count in reversed(range(1, countdown + 1)):
                print("You have", count, "trial left")
                guesses = int(input("Enter your guesses: "))
                rand_number = random.randrange(1, 10)
                if (guesses == rand_number):
                    print("You got it right")
                else:
                    print("That was wrong")
                    guess += 1
                
    elif (level==2):
        print("Choose a number between 1-50 and you have 4 guesses")
        guess=1
        while guess < 5:
            countdown =4
            for count in reversed(range(1, countdown + 1)):
                print("You have", count, "trial left")
                guesses = int(input("Enter your guesses: "))
                rand_number2 = random.randrange(1, 20)
                if (guesses == rand_number2):
                    print("You got it right")
                else:
                    print("That was wrong")
                    guess += 1
    else:
        print("Choose a number between 1-50 and you have 3 guesses")
        guess = 1
        while guess < 4:
            countdown = 3
            for count in reversed(range(1, countdown + 1)):
                print("You have", count, "trial left")
                guesses = int(input("Enter your guesses: "))
                rand_number3 = random.randrange(1, 50)
                if (guesses == rand_number3):
                    print("You got it right")
                else:
                    print("That was wrong")
                    guess +=1

guessing_game()

