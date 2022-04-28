import poker_hand as h
import main as m
import card as c


card_list = ['9 Clubs', '9' 'Hearts', '14' 'Spades', '11' 'Clubs', '12' 'Spades', '14' 'Clubs']

c4 = c.Card(4, 'Spades')
c5 = c.Card(5, 'Spades')
c6 = c.Card(6, 'Clubs')
c7 = c.Card(7, 'Hearts')
c8 = c.Card(8, 'Diamonds')
c9 = c.Card(9, 'Spades')
c10 = c.Card(10, 'Clubs')
c11 = c.Card(11, 'Spades')
c12 = c.Card(12, 'Spades')
c13 = c.Card(13, 'Hearts')


card_list1 = [c4, c5, c6, c5, c8]
card_list3 = [c13, c12, c12, c12, c8]

hand1 = h.PokerHand(card_list1)
hand3 = h.PokerHand(card_list3)


card_list2 = [c13, c9, c6, c8, c13]  # pair
card_list4 = [c13, c9, c6, c10, c13]  # pair
hand2 = h.PokerHand(card_list2)
hand4 = h.PokerHand(card_list4)

print(hand2.get_hand_ranks())
print(hand2.get_pairs())
print('')
print(hand4.get_hand_ranks())
print(hand4.get_pairs())

print(hand2.compare_to(hand4)) #-1
print(hand2.compare_pair(hand4))

