"""
models a card
"""

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
SUITS = ["Diamonds", "Clubs", "Hearts", "Spades"]  # do we have to use the word or can we represent using letters


class Card:

    def __init__(self, rank, suit):
        """
        card constructor
        :param rank: a card rank
        :param suit: a card suit
        """
        self.__rank = rank
        self.__suit = suit

    def get_rank(self):
        """
        :return: rank
        """
        return self.__rank

    def get_suit(self):  # this function will have to work differently now that the suit entire word is typed out
        """
        :return: suit
        """
        return self.__suit

    def __str__(self):
        return f'{self.__rank} {self.__suit}'

    def __repr__(self):
        return f'{self.__rank} {self.__suit}'