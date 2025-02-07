import random

random_numb = random.randint(0,1)
if random_numb == 1:
    print("Heads")
else:
    print("Tails")

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
friend_rand_index = random.randint(0, len(friends)-1)
print(f"{friends[friend_rand_index]} is to pay.")