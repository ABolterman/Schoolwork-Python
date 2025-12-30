from DeckClass import Deck


def find_best_hand(hand, shared_cards):
    # Royal Flush = 1
    # Straight Flush = 2
    # Four of a Kind = 3
    # Full House = 4
    # Flush = 5
    # Straight = 6
    # 3 of a kind = 7
    # Two Pair = 8
    # Pair = 9
    # High Card = 10

    # Adds values of all cards to list
    card_vals = []
    for index in range(2):
        card_vals += [hand[index].get_value()]
    for index in range(len(shared_cards)):
        card_vals += [shared_cards[index].get_value()]

    type = None
    curr_best_hand = None
    set_cards = shared_cards[:] + hand[:]
    all_cards = []

    # sort all_cards in desc order
    card_vals.sort(reverse=True)  # desc order
    for val in card_vals:
        index = 0
        for card in set_cards:
            if card.get_value() == val:
                all_cards.append(card)
                set_cards.pop(index)
            index += 1

    flush = False
    suits = [Deck.Card(Deck.SPADE, 1), Deck.Card(Deck.HEART, 1), Deck.Card(Deck.CLUB, 1), Deck.Card(Deck.DIAMOND, 1)]
    flush_copy = all_cards[:]

    for suit in suits:
        current_suit = suit.get_suit()
        suit_max = 0
        flush_cards = []
        for card in flush_copy:
            if current_suit == card.get_suit():
                suit_max += 1
                flush_cards.append(card)
        if suit_max >= 5:
            # a flush exists
            flush = True
            type = 5  # a flush type = current best type
            curr_best_hand = flush_cards[:]
            break

    if flush:
        for i in range(len(curr_best_hand) - 4):
            if curr_best_hand[i].get_value() == (curr_best_hand[i + 1].get_value() + 1) \
                    == (curr_best_hand[i + 2].get_value() + 2) == (curr_best_hand[i + 3].get_value() + 3) \
                    == (curr_best_hand[i + 4].get_value() + 4):
                if curr_best_hand[i].get_value() == 14:
                    type = 1
                else:
                    type = 2
                curr_best_hand = curr_best_hand[i:i + 5]
                break
        while len(curr_best_hand) > 5:
            curr_best_hand.pop()

    copy_vals = card_vals[:]
    copy_all = all_cards[:]
    all_cards_same = []
    all_same_maxes = []
    index = 0
    while index < 7:
        cards_same = []
        count = copy_vals.count(copy_vals[index])
        if count > 1:
            cards_same = copy_all[index:index + count]
            all_cards_same += cards_same
            all_same_maxes.append(count)
        index += count

    if len(all_same_maxes) != 0:
        if max(all_same_maxes) == 4:
            type = 3  # four of a kind, just return because highest if it has come to this point
            index = 0
            while not (all_cards_same[index].get_value() == all_cards_same[index + 1].get_value()
                       == all_cards_same[index + 2].get_value() == all_cards_same[index + 3].get_value()):
                index += 1
            curr_best_hand = all_cards_same[index:index + 4]
            for card in all_cards:
                if card.get_value() != curr_best_hand[0].get_value():
                    curr_best_hand += [card]
                    break
            return curr_best_hand, type

        if len(all_same_maxes) == 1:
            if max(all_same_maxes) == 3:
                type = 7
                curr_best_hand = all_cards_same[:]
                for card in all_cards:
                    if card.get_value() != curr_best_hand[0].get_value():
                        curr_best_hand += [card]
                        if len(curr_best_hand) == 5:
                            break
            else:
                type = 9
                curr_best_hand = all_cards_same[:]
                for card in all_cards:
                    if card.get_value() != curr_best_hand[0].get_value():
                        curr_best_hand += [card]
                        if len(curr_best_hand) == 5:
                            break

        if len(all_same_maxes) >= 2:
            if 3 in all_same_maxes:  # full house, but could be 3,2,2
                type = 4
                if all_same_maxes[0] == 3:
                    curr_best_hand = all_cards_same[0:5]
                elif all_same_maxes[1] == 3:
                    curr_best_hand = all_cards_same[2:5]
                    curr_best_hand += all_cards_same[0:2]
                else:
                    curr_best_hand = all_cards_same[5:8]
                    curr_best_hand += all_cards_same[0:2]
            else:  # If no 3, then pairs
                type = 8
                curr_best_hand = all_cards_same[0:4]
                for card in all_cards:
                    if card.get_value() != curr_best_hand[0].get_value() and card.get_value()\
                            != curr_best_hand[2].get_value():
                        curr_best_hand += [card]
                        break

    # have all_cards in desc
    # have all_vals in desc
    straight_1 = all_cards[:-2]
    straight1_vals = card_vals[:-2]
    straight_2 = all_cards[1:-1]
    straight2_vals = card_vals[1:-1]
    straight_3 = all_cards[2:]
    straight3_vals = card_vals[2:]

    if straight1_vals[0] == (straight1_vals[1] + 1) == (straight1_vals[2] + 2) == (straight1_vals[3] + 3) == (
            straight1_vals[4] + 4):
        # have a straight
        if type is not None:
            if type < 6:
                pass
            else:
                type = 6
                return straight_1, type
        else:
            type = 6
            return straight_1, type

    if straight2_vals[0] == (straight2_vals[1] + 1) == (straight2_vals[2] + 2) == (straight2_vals[3] + 3) == (
            straight2_vals[4] + 4):
        if type is not None:
            if type < 6:
                pass
            else:
                type = 6
                return straight_2, type
        else:
            type = 6
            return straight_2, type

    if straight3_vals[0] == (straight3_vals[1] + 1) == (straight3_vals[2] + 2) == (straight3_vals[3] + 3) == (
            straight3_vals[4] + 4):
        if type is not None:
            if type < 6:
                pass
            else:
                type = 6
                return straight_3, type
        else:
            type = 6
            return straight_3, type

    if curr_best_hand is None and type is None:
        return all_cards[:-2], 10  # type = 10, because in desc order - all_cards[0] is highest card
    else:
        return curr_best_hand, type


def compare_hands(player_hand, player_hand_type, computer_hand, computer_hand_type):
    # check which number is higher if same (lower is winner) -> then some extra coding
    if player_hand_type < computer_hand_type:
        return "player"
    elif computer_hand_type < player_hand_type:
        return "computer"
    else:  # computer_hand_type == player_hand_type
        if computer_hand_type == 1:
            return "tie"
        elif player_hand_type == 2:
            if computer_hand[0].get_value() > player_hand[0].get_value():
                return "computer"
            elif player_hand[0].get_value() > computer_hand[0].get_value():
                return "player"
            else:
                return "tie"
        elif player_hand_type == 3 or player_hand_type == 4 or player_hand_type == 5 or player_hand_type == 6 or \
                player_hand_type == 7:
            # which four of a kind card value is higher determines winner, can't be two four-of-a-kinds of same value
            # coded so the three of a kind is always indexes 0-2 so first card shows three of a kind values
            # desc order so highest card should already be first of the set
            if computer_hand[0].get_value() > player_hand[0].get_value():
                return "computer"
            elif player_hand[0].get_value() > computer_hand[0].get_value():
                return "player"

        elif player_hand_type == 8:
            if computer_hand[0].get_value() > player_hand[0].get_value():  # higher pair
                return "computer"
            elif player_hand[0].get_value() > computer_hand[0].get_value():
                return "player"
            else:  # equal pair
                if computer_hand[2].get_value() > player_hand[2].get_value():  # higher pair
                    return "computer"
                elif player_hand[2].get_value() > computer_hand[2].get_value():
                    return "player"
                else:  # second pair also equal
                    if computer_hand[4].get_value() > player_hand[4].get_value():  # higher card
                        return "computer"
                    elif player_hand[4].get_value() > computer_hand[4].get_value():
                        return "player"
                    else:
                        return "tie"
        elif player_hand_type == 9:
            if computer_hand[0].get_value() > player_hand[0].get_value():  # higher pair
                return "computer"
            elif player_hand[0].get_value() > computer_hand[0].get_value():
                return "player"
            else:
                for index in range(2, 5):
                    if computer_hand[index].get_value() > player_hand[index].get_value():  # higher pair
                        return "computer"
                    elif player_hand[index].get_value() > computer_hand[index].get_value():
                        return "player"
                return "tie"

        elif player_hand_type == 10:
            for index in range(5):
                if computer_hand[index].get_value() > player_hand[index].get_value():  # highest hard and down
                    return "computer"
                elif player_hand[index].get_value() > computer_hand[index].get_value():
                    return "player"
            return "tie"


def find_odds(computer_hand, shared_cards):
    # Creating test deck to draw cards from
    computer_wins = 0
    deck_copy = Deck()
    for card in computer_hand:
        for index in range(len(deck_copy.cards)):
            if deck_copy.cards[index] == card:
                deck_copy.cards.pop(index)
                break
    # Copies shared cards & removes from deck_copy
    if len(shared_cards) != 0:
        shared_cards_copy = shared_cards[:]
        for card in shared_cards:
            for index in range(len(deck_copy.cards)):
                if deck_copy.cards[index] == card:
                    deck_copy.cards.pop(index)
                    break
    else:
        shared_cards_copy = []

    # Changes the sample size based on how many cards revealed
    # match, case is essentially if elif statements -
    #   https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
    n = len(shared_cards_copy)
    match n:
        case 0:
            n = 200_000  # out of 2,097,572,400 possible combinations, about .01% (1% made my laptop cry)
        case 3:
            n = 10_000  # out of 1,070,190 possible combinations, about 1%
        case 4:
            n = 4_500  # out of 45,540 possible combinations, about 10%
        case 5:
            n = 990  # out of 990 possible combinations

    for index in range(0, n):
        testing_deck = Deck(deck_copy.cards[:])
        testing_shared = shared_cards_copy[:]
        player_hand = [testing_deck.deal_card(), testing_deck.deal_card()]
        while len(testing_shared) < 5:
            testing_shared.append(testing_deck.deal_card())
        computer_best, computer_hand_type = find_best_hand(computer_hand, testing_shared)
        test_player_best, player_hand_type = find_best_hand(player_hand, testing_shared)
        winner = compare_hands(test_player_best, player_hand_type, computer_best, computer_hand_type)
        if winner == "computer":
            computer_wins += 1

    return computer_wins / n
