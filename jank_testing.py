import poker_hand as h
import main as m
import card as c


card_list = ['9 Clubs', '9' 'Hearts', '14' 'Spades', '11' 'Clubs', '12' 'Spades', '14' 'Clubs']

card1 = c.Card('5', 'Spades')
card2 = c.Card('5', 'Clubs')
card3 = c.Card('5', 'Hearts')
card4 = c.Card('5', 'Diamonds')

card5 = c.Card('6', 'Spades')
card6 = c.Card('6', 'Clubs')

card7 = c.Card('7', 'Spades')

card8 = c.Card('8', 'Spades')


card_list1 = [card1, card2, card3, card4, card5] #true
card_list2 = [card1, card2, card5, card6, card7] #true
card_list3 = [card1, card2, card5, card7, card8] #false

hand1 = h.Hand(card_list1)
hand2 = h.Hand(card_list2)
hand3 = h.Hand(card_list3)


#print(hand1.is_pair())
print(hand1.get_pairs())
print(hand2.get_pairs())
print(hand3.get_pairs())
