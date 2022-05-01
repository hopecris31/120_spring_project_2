"""
main, runs the game
"""

import poker_hand as h
import deck as d

HAND_SIZE = 5


def __get_hand_cards(hand_size, deck):
    """
    :param hand_size: size of hand
    :param deck: a deck of cards
    :return: a list of card objects
    """
    cards = []
    for i in range(hand_size):
        new_card = deck.deal()
        cards.append(new_card)
    return cards


def main():
    deck = d.Deck()
    deck.shuffle()
    correct_guesses = 0

    game = True
    print("Enter 1 if hand 1 is better,  2 (or -1, idc im not the boss of you) if hand 2 is better, or 0 if it's a tie")
    while game and deck.enough_in_deck(HAND_SIZE):
        card_list1 = __get_hand_cards(HAND_SIZE, deck)
        card_list2 = __get_hand_cards(HAND_SIZE, deck)

        hand1 = h.PokerHand(card_list1)
        hand2 = h.PokerHand(card_list2)

        print('')
        print("HAND 1: ", str(hand1))
        print("HAND 2: ", str(hand2))
        print('')

        correct_answer = hand1.compare_to(hand2)
        user_answer = int(input("YOUR GUESS: "))

        if correct_answer == -1:
            correct_answer = 2
        if user_answer == -1:
            user_answer = 2
        if correct_answer == user_answer:
            correct_guesses += 1
        else:
            game = False

        print("correct answer: ", "HAND", correct_answer, "| your answer: ", "HAND", user_answer)
        print("correct guesses: ", correct_guesses)
        if not game:
            print("GAME OVER")
        if not deck.enough_in_deck(HAND_SIZE):
            print("All hands have been dealt!")


if __name__ == "__main__":
    main()
