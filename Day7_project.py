import random
from hangman_art import stages, logo
from hangman_word_list import word_list

placeholder = ""
game_over = False

print(logo)

chosen_word = random.choice(word_list)

for letter in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print("You lose a live.")
        if lives == 0:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])
