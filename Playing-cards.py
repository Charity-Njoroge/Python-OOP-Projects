"""
Classes to represent playing cards, deck of cards and poker hands
"""

import random


class Card(object):
    """ A representation of a card """

    # the default card is 2 of Clubs
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    # class attribute
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['None', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names
        [self.suit])

    # comparing cards using cmp method
    def __cmp__(self, other):
        # compare suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        # if suits are equal compare ranks
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        # if cards are equal
        return 0


class Deck(object):
    """ A representation of a deck"""

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    # printing a deck of cards
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    # add, remove, shuffle and sort cards in a deck
    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        return self.cards.append(card)

    def shuffle_cards(self):
        random.shuffle(self.cards)

    # method to move cards from deck to a hand
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


# def sort_cards(self):
# self.cards.sort(cmp=Card.__cmp__)


class Hand(Deck):
    """ A hand that is taken from a deck of cards. Inherits deck methods"""

    # override deck __init__ method
    def __init__(self, label=''):
        super().__init__()
        self.cards = []
        self.label = label

    def __str__(self):
        super().__str__()


# driver code
deck = Deck()
print(deck)
hand1 = Hand('First hand')
deck.move_cards(hand1, 4)
print(hand1.label, hand1.cards)
