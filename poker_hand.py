"""
models a poker hand
"""


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

    def __get_hand_ranks(self):
        """
        gets the ranks of the cards in a hand
        :return: the ranks of the hand
        """
        hand_ranks = []
        for card in self.__hand:
            rank = card.get_rank()
            hand_ranks.append(rank)
        return hand_ranks

    def __is_flush(self):
        """
        checks if the card hand is a flush
        :return: True if all card suits match, False if not
        """
        first_suit = self.__hand[0].get_suit()
        for card in self.__hand:
            if first_suit != card.get_suit():
                return False
        return True

    def __is_pair(self):
        """
        determines if a hand is a pair
        :return: True if pair, False if not
        """
        ranks = self.__get_hand_ranks()
        for card1 in range(len(ranks)):
            for card2 in range(card1 + 1, (len(ranks))):
                if ranks[card1] == ranks[card2]:
                    return True
        return False

    def __is_two_pair(self):
        """
        determines if a hand is a two pair
        :return: True if two pair, False if not
        """
        if self.__is_pair():
            pairs = 0
            ranks = self.__get_hand_ranks()
            for card1 in range(len(ranks)):
                for card2 in range(len(ranks) - card1 - 1):
                    if ranks[card1] == ranks[card2 + card1 + 1]:
                        pairs += 1
                        ranks[card1] = 1
                        ranks[card1 + card2 + 1] = -1
                        if pairs == 2:
                            return True
        return False

    def __is_three_kind(self):
        """
        identifies if a hand is three of a kind
        :return: True of three of a kind, False if not
        """
        ranks = self.__get_hand_ranks()
        ranks_by_occurrence = sorted(ranks, key=ranks.count, reverse=True)
        if ranks_by_occurrence.count(ranks_by_occurrence[0]) == 3:
            return True
        else:
            return False

    def __is_four_kind(self):
        """
        identifies if a hand is a four of a kind
        :return: True if four of a kind, False if not
        """
        ranks = self.__get_hand_ranks()
        ranks_by_occurrence = sorted(ranks, key=ranks.count, reverse=True)
        if ranks_by_occurrence.count(ranks_by_occurrence[0]) == 4:
            return True
        else:
            return False

    def __get_pairs(self):
        """
        identifies a pair in a hand, and adds it to a list
        :return: list of pair ranks
        """
        list_pairs = []

        if self.__is_pair():
            for card1 in range(len(self.__get_hand_ranks())):
                for card2 in range(card1 + 1, len(self.__get_hand_ranks())):
                    if self.__hand[card1].get_rank() == self.__hand[card2].get_rank() and self.__hand[card1].get_rank()\
                            not in list_pairs:
                        list_pairs.append(self.__hand[card1].get_rank())
        return list_pairs

    def __compare_hand_same_type(self, other):
        """
        if a hand is of the same type, returns the hand with the higher ranks
        :param other: a second pair
        :return: 1 if self has higher value hand, -1 of other has higher value hand, and 0 if tie
        """

        self_pair = self.__get_pairs()
        other_pair = other.__get_pairs()
        self_pair.sort(reverse=True)
        other_pair.sort(reverse=True)

        if self.__is_pair() and other.__is_pair():
            for i in range(len(self_pair)):
                if self_pair[i] > other_pair[i]:
                    return 1
                elif self_pair[i] < other_pair[i]:
                    return -1
        return self.__compare_high_card(other)

    def __compare_high_card(self, other):
        """
        orders the hand from least to greatest, then compares each of the highest values.
        keeps comparing until the highest card is found
        :param other: a second poker hand
        :return: 1 if self has highest card, -1 of other has highest card, and 0 if tie
        """

        self_ranked = self.__get_hand_ranks()
        other_ranked = other.__get_hand_ranks()

        self_ranked = sorted(self_ranked, reverse=True)
        other_ranked = sorted(other_ranked, reverse=True)

        for i in range(len(self_ranked)):
            if self_ranked[i] > other_ranked[i]:
                return 1
            elif self_ranked[i] < other_ranked[i]:
                return -1
        return 0

    def __hand_type_worth(self):
        """
        determines the worth of a hand by giving it a numeric value
        :return: the value of the hand type
        """
        if self.__is_flush():
            return 4
        elif self.__is_four_kind():
            return 3  # project description defines 4 of a kind as a 2 pair
        elif self.__is_two_pair():
            return 3
        elif self.__is_three_kind():
            return 2  # project description defines 3 of a kind as a pair
        elif self.__is_pair():
            return 2
        else:
            return 1

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
        self_hand_worth = self.__hand_type_worth()
        other_hand_worth = other.__hand_type_worth()

        if self_hand_worth > other_hand_worth:
            return 1
        if other_hand_worth > self_hand_worth:
            return -1

        if self_hand_worth == other_hand_worth:
            return self.__compare_hand_same_type(other)

        return self.__compare_high_card(other)

    def __repr__(self):
        return str(self.__hand)
