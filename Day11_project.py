import random
from blackjack_art import logo


def deal_card():
    """Deals card randomly from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calc_score(cards):
    """Sums up card list"""
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
#
#
# def blackjack_win(player, dealer):
#     if player


def compare_score(player, dealer):
    """Compares players scores to get winner"""
    if dealer == 0:
        return "Blackjack!! You win!!"
    elif player == 0:
        return "Computer Blackjack, You lose!"
    elif player > 21:
        return "You went over 21, you lose!"
    elif dealer > 21:
        return "You win!"
    elif player > dealer:
        return "You win!"
    elif player == dealer:
        return "It's a draw"
    else:
        return "You lose!"


def play_blackjack():
    """Game logic/process"""
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    print("\n" * 100)
    play_blackjack()
