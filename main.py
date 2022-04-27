"""
main, runs the game
"""
import poker_hand as h
import deck as d


def get_hand_cards(hand_size):
    cards = []
    for i in range(hand_size):
        new_card = deck.deal()
        cards.append(new_card)
    return cards


if __name__ == "__main__":
    deck = d.Deck()
    deck.shuffle()
    correct_guesses = 0

    game = True
    print("Enter 1 if hand 1 is better, -1 if hand 2 is better, or 0 if it's a tie")
    while game:  # change condition to while deck not empty, or while enough cards for hand

        card_list1 = get_hand_cards(h.DEFAULT_HAND_SIZE)
        card_list2 = get_hand_cards(h.DEFAULT_HAND_SIZE)

        hand1 = h.Hand(card_list1)
        hand2 = h.Hand(card_list2)

        print('')
        print("Hand 1: ", hand1)
        print("Hand 2: ", hand2)
        print('')

        correct_answer = hand1.compare_to(hand2)
        user_answer = int(input("YOUR GUESS: "))

        if hand1.compare_to(hand2) == user_answer:
            correct_guesses += 1  # why not adding one to correct guesses
            print("correct answer: ", correct_answer, "your answer: ", user_answer)
            print("correct guesses: ", correct_guesses)
        else:
            game = False
            print("correct answer: ", correct_answer, "your answer: ", user_answer)
            print("correct guesses: ", correct_guesses)




"""
    card_listA = get_hand_cards(h.DEFAULT_HAND_SIZE)
    card_listB = get_hand_cards(h.DEFAULT_HAND_SIZE)

    handA = h.Hand(card_listA)
    handB = h.Hand(card_listB)

    print(handA)
    print(handB)

    print(handA.compare_to(handB))
"""




"""
for index in range(DEFAULT_HAND_SIZE + 1):
    card = self.__temp_deck.deal()
    hand.append(card)
"""