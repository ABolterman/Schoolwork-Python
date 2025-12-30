import random


class Deck:
    SPADE = "♠"
    HEART = "♥"
    CLUB = "♣"
    DIAMOND = "♦"

    class Card:
        def __init__(self, suit, value):
            # Jack, Queen, King, Ace = 11, 12, 13, 14 respectfully
            self._suit = suit
            self._value = value

        def __str__(self):
            suit = self.get_suit()
            match suit:
                case 1:
                    suit_name = "Spades"
                case 2:
                    suit_name = "Hearts"
                case 3:
                    suit_name = "Clubs"
                case 4:
                    suit_name = "Diamonds"
            return f"{suit_name}: {self.get_value()}"

        def get_suit(self):
            return self._suit

        def get_suit_str(self):
            suit = self.get_suit()
            match suit:
                case 1:
                    suit_name = "Spades"
                case 2:
                    suit_name = "Hearts"
                case 3:
                    suit_name = "Clubs"
                case 4:
                    suit_name = "Diamonds"
            return suit_name

        def get_value(self):
            return self._value

        def __eq__(self, other):
            if self._suit == other._suit and self._value == other._value:
                return True
            else:
                return False

    def __init__(self, cards=None):
        if cards:
            self.cards = cards
        else:
            self.cards = []
            for value in range(2, 15):
                self.cards.append(self.Card(Deck.SPADE, value))
                self.cards.append(self.Card(Deck.HEART, value))
                self.cards.append(self.Card(Deck.CLUB, value))
                self.cards.append(self.Card(Deck.DIAMOND, value))

    def deal_card(self):
        card_index = random.randint(0, len(self.cards) - 2)
        return self.cards.pop(card_index)
