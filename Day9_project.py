# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "times_visited": 8
#     },
#     "Germany": {
#         "cities_visited": ["Hamburg", "Stuttgart", "Berlin"],
#         "times_visited": 12
#     },
# }

# for letters in (travel_log["Germany"]["cities_visited"][1]):
#     print(letters)

# nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

# Blind auction program

print("Welcome")

bid_over = False
blind_auction = {}
highest_bid = 0

while not bid_over:
    name = input("What's your name: ")
    bid = int(input("What's your bid: $"))
    more_bidder = input("Are there any more bidder? Type 'yes' or 'no': ").lower()
    blind_auction[name] = bid
    if more_bidder == "no":
        bid_over = True
    elif more_bidder != "yes":
        print("Invalid reply")
        more_bidder = input("Are there any more bidder? Type 'yes' or 'no': ").lower()

for key in blind_auction:
    if blind_auction[key] > highest_bid:
        highest_bid = blind_auction[key]

print(highest_bid)