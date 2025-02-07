import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

play = [rock, paper, scissors]

user_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.choice(play)
user_choice = play[user_num]
print(user_choice)
print(f"Computer chose:{computer_choice}")
if user_num == 0 and computer_choice == play[2] or user_num == 1 and computer_choice == play[0] or\
        user_num == 2 and computer_choice == play[1]:
    print("You win")

elif play[user_num] == computer_choice:
    print("It's a draw")
else:
    print("You lose")
