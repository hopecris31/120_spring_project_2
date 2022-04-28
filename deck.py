"""
models a deck of cards
"""
import random
import card as c

HAND_SIZE = 5


class Deck:

    def __init__(self):
        """
        deck constructor
        """
        self.__deck = []
        self.__create_deck()

    def __create_deck(self):
        for i in range(len(c.RANKS)):
            for j in range(len(c.SUITS)):
                card = c.Card(c.RANKS[i], c.SUITS[j])
                self.__deck.append(card)

    def shuffle(self):
        """
        shuffles a deck of cards
        :return: the shuffled deck of cards as a list
        """
        return random.shuffle(self.__deck)

    def enough_in_deck(self):
        """
        checks if there are enough cards in the deck to make another hand
        :return: True or False, depending if there are enough cards
        """
        if len(self.__deck) >= HAND_SIZE:
            enough = True
        else:
            enough = False
        return enough

    def deal(self):
        """
        deals a single card from the top of the deck
        :return: a card, or None if empty
        """
        if len(self.__deck) == 0:
            return None
        else:
            return self.__deck.pop(0)

