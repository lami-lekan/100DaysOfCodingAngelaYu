# number guessing game
import random


def guessing_game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between  1 and 100.")
    num_to_guess = random.randint(1, 100)
    attempts = 0
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        attempts += 10
    elif level == 'hard':
        attempts += 5
    else:
        print("Sorry type a correct input")
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    guess = int(input(f"You have {attempts} remaining to guess the number.\nMake a guess: "))

    while attempts > 1:
        if num_to_guess > guess:
            print("Too low.\nGuess again.")
            attempts -= 1
            guess = int(input(f"You have {attempts} remaining to guess the number.\nMake a guess: "))
        elif num_to_guess < guess:
            print("Too high.\nGuess again.")
            attempts -= 1
            guess = int(input(f"You have {attempts} remaining to guess the number.\nMake a guess: "))
        else:
            print(f"You guessed the number {num_to_guess} right.")
            break
    else:
        print(f"You've run out of guesses. Refresh the page to run again.")


guessing_game()
