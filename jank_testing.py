import poker_hand as h
import unit_testing as u
import card as c


card_list = ['9 Clubs', '9' 'Hearts', '14' 'Spades', '11' 'Clubs', '12' 'Spades', '14' 'Clubs']

c2 = c.Card(2, 'Spades')
c3 = c.Card(3, 'Spades')
c4 = c.Card(4, 'Spades')
c5 = c.Card(5, 'Spades')
c6 = c.Card(6, 'Spades')
c7 = c.Card(7, 'Hearts')
c8 = c.Card(8, 'Hearts')
c9 = c.Card(9, 'Hearts')
c10 = c.Card(10, 'Hearts')
c11 = c.Card(11, 'Hearts')
c12 = c.Card(12, 'Hearts')
c13 = c.Card(13, 'Hearts')
c14 = c.Card(14, 'Hearts')

s2 = c.Card(2, 'Spades')
s3 = c.Card(3, 'Spades')


card_list1 = [c10, c5, c6, c10, c5]
card_list1b = [c14, c5, c4, c12, c7]

card_list3 = [c3, c12, c12, c12, c2] # three pair
card_list3b = [c12, c12, c10, c12, c3] # inferior three pair

hand1 = h.PokerHand(card_list1)
hand1b = h.PokerHand(card_list1b)
hand3 = h.PokerHand(card_list3)
hand3b = h.PokerHand(card_list3b)




card_list2 = [c13, c13, c13, c13, s3]  # pair
card_list4 = [c10, s2, c10, c10, c10]  # pair
hand2 = h.PokerHand(card_list2)
hand4 = h.PokerHand(card_list4)


print(hand4.get_hand_type())
print(hand2.get_hand_type())
if hand4.get_hand_type() == hand2.get_hand_type():
    print('yes')

#print(hand1.compare_to(hand1b))
#print(hand3.compare_to(hand3b))
print(u.pair5.compare_to(u.two_pair5))
#print(hand3.is_three_pair())
#print(hand2.is_four_pair())
#print(hand4.is_four_pair())
#print(hand2.get_hand_ranks)
#print(hand2.compare_to(hand4)) #-1

#print(hand2.get_pairs())

