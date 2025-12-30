from DeckClass import Deck
from CompairingStuff import find_best_hand
from CompairingStuff import find_odds
from CompairingStuff import compare_hands

player_money = 100
computer_money = 100
play = "Y"


def display_cards(hand):
    for index in range(0, len(hand)):
        value = hand[index].get_value()
        match value:
            case 11:
                value = "J"
            case 12:
                value = "Q"
            case 13:
                value = "K"
            case 14:
                value = "A"

        if index != len(hand) - 1:
            print(f"{hand[index].get_suit()}{value}", end=", ")
        else:
            print(f"{hand[index].get_suit()}{value}", end="")
    print()


def betting(pool, player_money, computer_money, computer_hand, shared_cards, player_hand):
    print(f"The current betting pool is ${pool}.")
    print(f"Your odds of winning are {find_odds(player_hand, shared_cards)}")
    player_bet = int(input("How much do you want to bet?"))
    while player_bet > player_money or player_bet > computer_money:
        print("Your bet can't be higher than your or the computer's total money.")
        print(f"You have ${player_money} and the computer has ${computer_money}.")
        player_bet = int(input("How much do you want to bet?"))
    pool += player_bet
    player_money -= player_bet
    if player_bet == 0:
        computer_move = "call"
    else:
        odds = find_odds(computer_hand, shared_cards)
        if odds >= .5:
            computer_move = "call"
            computer_money -= player_bet
            pool += player_bet
        else:
            computer_move = "fold"
            player_money += pool
    return pool, player_money, computer_money, computer_move


while play == "Y":
    # Round set up
    pool = 0
    deck = Deck()
    shared_cards = []

    # Initial deal
    player_hand = [deck.deal_card(), deck.deal_card()]
    print("Your cards are", end=" ")
    display_cards(player_hand)
    computer_hand = [deck.deal_card(), deck.deal_card()]

    # Betting
    pool, player_money, computer_money, computer_move \
        = betting(pool, player_money, computer_money, computer_hand, shared_cards, player_hand)
    if computer_move == "fold":
        print("The computer folded and you have won.")
        play = input("Play again? (Y/N)")
        continue

    # Dealing flop
    shared_cards.append(deck.deal_card())
    shared_cards.append(deck.deal_card())
    shared_cards.append(deck.deal_card())
    print("The shared cards are", end=" ")
    display_cards(shared_cards)
    print("Your cards are", end=" ")
    display_cards(player_hand)

    # Betting
    pool, player_money, computer_money, computer_move = \
        betting(pool, player_money, computer_money, computer_hand, shared_cards, player_hand)
    if computer_move == "fold":
        print("The computer folded.")
        print(f"You've won ${pool}")
        play = input("Play again? (Y/N)")
        continue

    # Dealing the turn
    shared_cards.append(deck.deal_card())
    print("The shared cards are", end=" ")
    display_cards(shared_cards)
    print("Your cards are", end=" ")
    display_cards(player_hand)

    # Betting
    pool, player_money, computer_money, computer_move = \
        betting(pool, player_money, computer_money, computer_hand, shared_cards, player_hand)
    if computer_move == "fold":
        print("The computer folded.")
        print(f"You've won ${pool}")
        play = input("Play again? (Y/N)")
        continue

    # Dealing the river
    shared_cards.append(deck.deal_card())
    print("The shared cards are", end=" ")
    display_cards(shared_cards)
    print("Your cards are", end=" ")
    display_cards(player_hand)

    # Betting
    pool, player_money, computer_money, computer_move \
        = betting(pool, player_money, computer_money, computer_hand, shared_cards, player_hand)
    if computer_move == "fold":
        print("The computer folded.")
        print(f"You've won ${pool}")
        play = input("Play again? (Y/N)")
        continue

    # Find best player hand
    player_best, play_type = find_best_hand(player_hand, shared_cards)
    computer_best, comp_type = find_best_hand(computer_hand, shared_cards)
    print("Your cards are", end=" ")
    display_cards(player_best)
    print("The computer's cards are", end=" ")
    display_cards(computer_best)

    # Compare hands
    winner = compare_hands(player_best, play_type, computer_best, comp_type)
    if winner == "tie":
        print(f"It was a tie. No one wins the money pool")
        player_money += pool / 2
        computer_money += pool / 2
    elif winner == "player":
        print(f"You win! You've won ${pool}")
        player_money += pool
    else:
        print("The computer won.")
        computer_money += pool

    if player_money == 0:
        print("You don't have any more money to play with")
        play = "N"
    elif computer_money == 0:
        print("The computer is out of money")
        play = "N"
    else:
        play = input("Play again? (Y/N)")

print(f"You now have ${player_money}")
