"""
models a poker hand
"""

DEFAULT_HAND_SIZE = 5
DEFAULT_HANDS_PER_DECK = 10  # a standard deck of 52 cards would be able to create 10 hands of 5 cards


class PokerHand:

    def __init__(self, card_list):
        """
        hand constructor
        :param card_list: a deck of cards
        """
        self.__hand = card_list.copy()

    def add_card(self, card):
        """
        adds a card to the hand
        :param card: a card
        :return: hand plus the added card
        """
        self.__hand.append(card)

    def get_hand_ranks(self):
        """
        gets the ranks of the cards in a hand
        :return: the ranks of the hand
        """
        hand_ranks = []
        for card in self.__hand:
            rank = card.get_rank()
            hand_ranks.append(rank)
        return hand_ranks

    def check_hand_type(self):
        """
        :param hand: a hand of 5 cards
        :return: the type of hand it is
        """

        if self.is_flush():
            return 'Flush'
        elif self.is_two_pair():
            return 'Two Pair'
        elif self.is_pair():
            return 'Pair'
        else:
            return 'High Card'

    def is_flush(self):
        """
        checks if the card hand is a flush
        :return: True if all card suits match, False if not
        """
        first_suit = self.__hand[0].get_suit()
        for card in self.__hand:
            if first_suit != card.get_suit():
                return False
        return True

    def is_pair(self):
        """
        checks hand, iterates one pair at a time and tries all card combinations for pairs.
        if pair is found, returns True.
        :return: True when a pair or three of a kind is detected
        """
        ranks = self.get_hand_ranks()
        for card1 in range(len(ranks)):
            for card2 in range(card1 + 1, (len(ranks))):
                if ranks[card1] == ranks[card2]:
                    return True
        return False

    def get_pairs(self):
        """
        identifies a pair in a hand, and adds it to a list
        :return: list of pair ranks
        """
        list_pairs = []
        if self.is_pair():
            for card1 in range(DEFAULT_HAND_SIZE-1):
                for card2 in range(card1 + 1, DEFAULT_HAND_SIZE):
                    if self.__hand[card1].get_rank() == self.__hand[card2].get_rank() and self.__hand[card1].get_rank() not in list_pairs:
                        list_pairs.append(self.__hand[card1].get_rank())
        return list_pairs

    def is_two_pair(self):
        """
        iterates through hand, determines if two pairs exist within the hand
        :return: True if there is a two pair, four of a kind, or full house
        """
        if self.is_pair():  # methods within a class do not take self as parameter?
            pairs = 0
            ranks = self.get_hand_ranks()
            for card in range(len(ranks)):
                for card_compare in range(len(ranks) - card - 1):
                    if ranks[card] == ranks[card + card_compare + 1]:
                        pairs += 1
                        ranks[card] = 'none'
                        ranks[card + card_compare + 1] = 'none1'
                        if pairs == 2:
                            return True
        return False

    def compare_high_card(self, other):
        """
        orders the hand from least to greatest, then compares each of the highest values.
        keeps comparing until the highest card is found
        :param other: a second poker hand
        :return: 1 if self has highest card, -1 of other has highest card, and 0 if tie
        """

        self_ranked = self.get_hand_ranks()
        other_ranked = other.get_hand_ranks()

        self_ranked = sorted(self_ranked, reverse=True)
        other_ranked = sorted(other_ranked, reverse=True)

        for i in range(0, len(self_ranked)):
            #print(str(self_ranked[i]) + str(other_ranked[i]))
            if self_ranked[i] > other_ranked[i]:
                return 1
            elif self_ranked[i] < other_ranked[i]:
                return -1
        return 0

    def compare_two_pair(self, other):
        """
        compares the ranks of each two pair, returns the two pair of higher rank.
        if both two pairs are the same, then compare the rank of remaining card
        :param other: a second two pair
        :return: 1 if self has higher value hand, -1 of other has highest value hand, and 0 if tie
        """

        self_pair = self.get_pairs()
        other_pair = other.get_pairs()

        self_pair = sorted(self_pair, reverse=True)
        other_pair = sorted(other_pair, reverse=True)

        if len(self_pair) == 2:
            for i in range(len(self_pair)):
                if self_pair[i] > other_pair[i]:
                    return 1
                elif self_pair[i] < other_pair[i]:
                    return -1
            return self.compare_high_card(other)

    def compare_pair(self, other):
        """
        compares the ranks of each pair, returns the pair of higher rank.
        if both pairs are the same, then compare the highest ranking remaining cards
        :param other: a second pair
        :return: 1 if self has higher value hand, -1 of other has highest value hand, and 0 if tie
        """

        self_pair = self.get_pairs()
        other_pair = other.get_pairs()

        self_pair.sort(reverse=True)
        other_pair.sort(reverse=True)

        if len(self_pair) == 1:
            for i in range(len(self_pair)):
                if self_pair[i] > other_pair[i]:
                    return 1
                elif self_pair[i] < other_pair[i]:
                    return -1
            return self.compare_high_card(other)

    def compare_to(self, other):
        """
         Determines which of two poker hands is worth more. Returns an int
         which is either positive, negative, or zero depending on the comparison.
         :param self: The first hand to compare
         :param other: The second hand to compare
         :return: a negative number if self is worth LESS than other_hand,
         zero if they are worth the SAME (a tie), and a positive number if
         self is worth MORE than other_hand
        """

        self_is_flush = self.is_flush()
        other_is_flush = other.is_flush()

        if self_is_flush and other_is_flush:
            return self.compare_high_card(other)
        elif self_is_flush and not other_is_flush:
            return 1
        elif not self_is_flush and other_is_flush:
            return -1

        self_is_two_pair = self.is_two_pair()
        other_is_two_pair = other.is_two_pair()

        if self_is_two_pair and other_is_two_pair:
            return self.compare_two_pair(other)
        elif self_is_two_pair and not other_is_two_pair:
            return 1
        elif not self_is_two_pair and other_is_two_pair:
            return -1

        self_is_pair = self.is_pair()
        other_is_pair = other.is_pair()

        if self_is_pair and other_is_pair:
            return self.compare_pair(other)
        elif self_is_pair and not other_is_pair:
            return 1
        elif not self_is_pair and other_is_pair:
            return -1

        return self.compare_high_card(other)

    def __str__(self):
        """
        :return:
        """
        return str(self.__hand)

    def __repr__(self):
        return str(self.__hand)