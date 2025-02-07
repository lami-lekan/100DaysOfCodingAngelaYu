# Higher or Lower Game
import random
from Day14_GameData import data
from Day14_GameLogo import logo, vs


# Todo 3: create compare function
def compare(option_aa, option_bb):
    if option_aa > option_bb:
        return 'a'
    else:
        return 'b'


# Todo 1: Print Game Logo
print(logo)
# Todo 2: create prints function
score = 0
game_over = False
first_num = random.randint(0, len(data)-1)
while not game_over:
    second_num = random.randint(0, len(data)-1)
    option_a = data[first_num]['follower_count']
    option_b = data[second_num]['follower_count']
    while first_num == second_num:
        second_num = random.randint(0, len(data))
    print(f"Compare A: {data[first_num]['name']},"
          f"a {data[first_num]['description']}, from {data[first_num]['country']}.")
    print(vs)
    print(f"Against B: {data[second_num]['name']},"
          f"a {data[second_num]['description']}, from {data[second_num]['country']}.")
    answer = input("Who has more follower 'A' or 'B': ").lower()
    correct_ans = compare(option_a, option_b)
    if answer == 'a' and correct_ans == 'a':
        score += 1
        print(f"You're right! Current score: {score}")
        first_num = second_num
    elif answer == 'b' and correct_ans == 'b':
        score += 1
        print(f"You're right! Current score: {score}")
        first_num = second_num
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
