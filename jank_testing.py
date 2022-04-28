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
card9 = c.Card('8', 'Hearts')


card_list1 = [card1, card2, card3, card4, card5]
card_list2 = [card1, card2, card5, card6, card7] #55667
card_list3 = [card1, card2, card5, card7, card8]
card_list4 = [card6, card6, card6, card4, card4] #66655

hand1 = h.Hand(card_list1)
hand2 = h.Hand(card_list2)
hand3 = h.Hand(card_list3)
hand4 = h.Hand(card_list4)


#print(hand1.is_pair())
#print(hand1.get_pairs())
#print(hand3.get_pairs())
print(hand2.get_pairs())
print(hand4.get_pairs())

#print(hand2.compare_to(hand4)) #-1
print(hand2.compare_two_pair(hand4))

#sort two pair ranks from greatest to least, sort is not working
#make a point system for the greater pair, check which is better