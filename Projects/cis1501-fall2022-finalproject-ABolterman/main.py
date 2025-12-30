import random
#source for how to align printing columns: https://www.geeksforgeeks.org/string-alignment-in-python-f-string/


# part 1 - Blackjack classes
# - use a shoe of 6 decks of cards
#    shuffle the shoe if the card count gets < 100 reshuffle
shoe = {1: 24, 2: 24, 3: 24, 4: 24, 5: 24, 6: 24, 7: 24, 8: 24, 9: 24, 10: 24, 11: 24, 12: 24, 13: 24}


class Card:
    def __init__(self, number):
        if number in range(2, 10):
            self._value = number
        elif number in range(10, 14):
            self._value = 10
        else:
            self._value = 11

    def get_value(self):
        return self._value

    def change_ace(self):
        self._value = 1


def deal_card(deck):
    number = random.randint(1, 13)
    # To check if card value still available
    while deck[number] == 0:
        number = random.randint(1, 13)
    deck[number] -= 1
    return Card(number)


# part 2 - Blackjack game using classes and user input - assume every hand is worth $1, tracking win/loss amount
p_or_s = input("Do you want to play or simulatate? (p/s)")
if p_or_s == "p":
    wins = 0
    losses = 0
    play = "y"
    while play != "n":
        player_hand = [deal_card(shoe), deal_card(shoe)]
        player_total = player_hand[0].get_value() + player_hand[1].get_value()
        dealer_hand = [deal_card(shoe), deal_card(shoe)]
        dealer_total = dealer_hand[0].get_value() + dealer_hand[1].get_value()
        print(f"The dealer's revealed card is worth {dealer_hand[0].get_value()}")
        if (player_total == 21 or dealer_total == 21) and len(player_hand) == 2:
            if player_total == 21 and dealer_total == 21:
                print("Both you and the dealer have blackjack, so it's a tie!")
            elif player_total == 21:
                print("You got blackjack!")
                print("You win!")
                wins += 1
            elif dealer_total == 21:
                print("The dealer got blackjack!")
                print("You lose.")
                losses += 1
            play = input("Play again? y/n")
            continue

        choice = "hit"
        while choice == "hit":
            print(f"Your cards are worth", end=" ")
            for card in player_hand:
                if card.get_value() == 11 and player_total > 21:
                    card.change_ace()
                    player_total -= 10
                print(card.get_value(), end=" ")
            print()

            print(f"for a total of {player_total}.")
            print()
            if player_total > 21:
                print("You bust!")
                print("You lose.")
                losses += 1
                break
            if player_total == 21:
                break

            choice = input("Do you want to hit or stay?")
            if choice == "hit":
                new_card = deal_card(shoe)
                player_hand.append(new_card)
                player_total += new_card.get_value()
                print(player_total)

        if player_total <= 21:
            dealer_total = dealer_hand[0].get_value() + dealer_hand[1].get_value()
            print(f"The dealer's cards are worth {dealer_hand[0].get_value()} and {dealer_hand[1].get_value()} "
                  f"for a total of {dealer_total}.")
            while dealer_total < 17:
                print(f"The dealer draws a card.")
                new_card = deal_card(shoe)
                dealer_hand.append(new_card)
                dealer_total += new_card.get_value()
                print(f"The dealer's cards are worth", end=" ")
                for card in dealer_hand:
                    if card.get_value() == 11 and dealer_total > 21:
                        card.change_ace()
                        dealer_total -= 10
                    print(card.get_value(), end=" ")
                print(f"for a total of {dealer_total}.")
                print()

            if dealer_total > 21:
                print("The dealer busts!")
                print("You win!")
                wins += 1
            elif dealer_total > player_total:
                print("You lose.")
                losses += 1
            elif dealer_total == player_total:
                print("You tie!")
            else:
                print("You win!")
                wins += 1

        total_cards = 0
        for key in shoe:
            total_cards += shoe[key]
        if total_cards < 100:
            shoe = {1: 24, 2: 24, 3: 24, 4: 24, 5: 24, 6: 24, 7: 24, 8: 24, 9: 24, 10: 24, 11: 24, 12: 24, 13: 24}
        play = input("Do you want to play again? y/n")
        print()
        print()

    print(f"You won {wins} times and lost {losses} times.")
    print(f"You earned {wins - losses} dollars.")

if p_or_s == "s":
    # Simulation for 100k hands, want a result table, winning strat (hit vs stand) for each starting value
    stay_dict = {}
    hit_dict = {}
    for i in range(4, 21):
        stay_dict[i] = [0, 0, 0]
        hit_dict[i] = [0, 0, 0]
    blackjacks = [0, 0, 0]
    #start money : [wins, losses, draws]
    for hand in range(100000):
        player_hand = [deal_card(shoe), deal_card(shoe)]
        player_total = player_hand[0].get_value() + player_hand[1].get_value()
        new_ptotal = player_total
        dealer_hand = [deal_card(shoe), deal_card(shoe)]
        dealer_total = dealer_hand[0].get_value() + dealer_hand[1].get_value()
        for card in player_hand:
            if card.get_value() == 11 and player_total > 21:
                card.change_ace()
                new_ptotal -= 10
                player_total -= 10
        if (player_total == 21 or dealer_total == 21) and len(player_hand) == 2:
            if player_total == 21 and dealer_total == 21:
                blackjacks[2] += 1 #draw
            elif player_total == 21:
                blackjacks[0] += 1 # a win
            elif dealer_total == 21:
                blackjacks[1] += 1
            continue

        val = "stay"
        choice = 1
        hand_round = 0
        while choice == 1:
            for card in player_hand:
                if card.get_value() == 11 and new_ptotal > 21:
                    card.change_ace()
                    new_ptotal -= 10

            if new_ptotal > 21:
                if val == "stay":
                    stay_dict[player_total][1] += 1 # stay loss
                if val == "hit":
                    hit_dict[player_total][1] += 1 # Hit loss
                break

            if new_ptotal == 21:
                # if val == "hit":
                #     hit_dict[player_total][0] += 1 #win
                # if val == "stay":
                #     stay_dict[player_total][0] += 1
                break

            if new_ptotal < 21 and hand_round == 0:
                choice = random.randint(1, 2)  # hit = 1, stay = 2
            else:
                choice = 2

            if choice == 1:
                new_card = deal_card(shoe)
                player_hand.append(new_card)
                new_ptotal += new_card.get_value()
                val = "hit"
                hand_round = 1

        if new_ptotal <= 21:
            dealer_total = dealer_hand[0].get_value() + dealer_hand[1].get_value()
            while dealer_total < 17:
                new_card = deal_card(shoe)
                dealer_hand.append(new_card)
                dealer_total += new_card.get_value()
                for card in dealer_hand:
                    if card.get_value() == 11 and dealer_total > 21:
                        card.change_ace()
                        dealer_total -= 10

            if dealer_total > 21:
                if val == "stay":
                    stay_dict[player_total][0] += 1 #win
                if val == "hit":
                    hit_dict[player_total][0] += 1
            elif dealer_total > new_ptotal:
                if val == "stay":
                    stay_dict[player_total][1] += 1 #loss
                if val == "hit":
                    hit_dict[player_total][1] += 1
            elif dealer_total == new_ptotal:
                if val == "stay":
                    stay_dict[player_total][2] += 1 #draw
                if val == "hit":
                    hit_dict[player_total][2] += 1
            else:
                if val == "stay":
                    stay_dict[player_total][0] += 1 #win
                if val == "hit":
                    hit_dict[player_total][0] += 1

        total_cards = 0
        for key in shoe:
            total_cards += shoe[key]
        if total_cards < 100:
            shoe = {1: 24, 2: 24, 3: 24, 4: 24, 5: 24, 6: 24, 7: 24, 8: 24, 9: 24, 10: 24, 11: 24, 12: 24, 13: 24}

    print(f'{"Hand Total" : <6}: {"Hit Wins" : ^6} | {"Hit Losses" : ^6} | {"Hit Draws" : ^6} | {"Stay Wins" : ^6} | '
          f'{"Stay Losses" : ^6} | {"Stay Draws" : >6}')
    for key in hit_dict:
        print(f" {key : <8} : {hit_dict[key][0] : ^8} | {hit_dict[key][1] : ^10} | {hit_dict[key][2] : ^10}| "
              f"{stay_dict[key][0] : ^9} | {stay_dict[key][1] : ^11} |{stay_dict[key][2] : >7}")
    print(f" 21 (immediate blackjacks): Wins: {blackjacks[0]}, Losses: {blackjacks[1]}, Draws: {blackjacks[2]}")



    # total_rounds = 0
    # for i in range(3):
    #     for key in hit_dict:
    #         total_rounds += hit_dict[key][i]
    #         total_rounds += stay_dict[key][i]
    #     total_rounds += blackjacks[i]
    #print(f"Total rounds = {total_rounds}")