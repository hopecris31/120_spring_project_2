"""
Unit testing, testing the compare_to() method
"""

import testing_suite as t
import card as c
import poker_hand as h
s2 = c.Card(2, 'Spades')
s3 = c.Card(3, 'Spades')
s4 = c.Card(4, 'Spades')
s5 = c.Card(5, 'Spades')
s6 = c.Card(6, 'Spades')
s7 = c.Card(7, 'Spades')
s8 = c.Card(8, 'Spades')
s9 = c.Card(9, 'Spades')
s10 = c.Card(10, 'Spades')
s11 = c.Card(11, 'Spades')
s12 = c.Card(12, 'Spades')
s13 = c.Card(13, 'Spades')
s14 = c.Card(14, 'Spades')

c2 = c.Card(2, 'Clubs')
c3 = c.Card(3, 'Clubs')
c4 = c.Card(4, 'Clubs')
c5 = c.Card(5, 'Clubs')
c6 = c.Card(6, 'Clubs')
c7 = c.Card(7, 'Clubs')
c8 = c.Card(8, 'Clubs')
c9 = c.Card(9, 'Clubs')
c10 = c.Card(10, 'Clubs')
c11 = c.Card(11, 'Clubs')
c12 = c.Card(12, 'Clubs')
c13 = c.Card(13, 'Clubs')
c14 = c.Card(14, 'Clubs')

h6 = c.Card(6, 'Hearts')
h10 = c.Card(10, 'Hearts')

d6 = c.Card(6, 'Diamonds')
d10 = c.Card(10, 'Diamonds')
d14 = c.Card(14, 'Diamonds')

flush1 = h.PokerHand([c10, c11, c12, c13, c14])  # highest flush hand
flush2 = h.PokerHand([s9, s8, s7, s6, s5, s4])  # second-highest flush hand
flush3 = h.PokerHand([c9, c8, c7, c6, c5, c4])  # same as hand above w different suits

two_pair1 = h.PokerHand([c14, s14, c10, s10, c4])
two_pair2 = h.PokerHand([c14, s14, c10, s10, s5])
two_pair3 = h.PokerHand([s10, c10, c9, s9, s2])
two_pair4 = h.PokerHand([c10, s10, c6, s6, c12])
two_pair5 = h.PokerHand([h10, d10, h6, d6, s12])
two_pair6 = h.PokerHand([c12, s12,c10, s10, c4])

pair1 = h.PokerHand([c11, s11, c5, s7, c2])
pair2 = h.PokerHand([s10, c10, c7, s14, c3]) # pair 10s
pair3 = h.PokerHand([h10, d10, h6, c7, s11])
pair4 = h.PokerHand([s10, c10, s6, s7, c11])
pair5 = h.PokerHand([s14, c14, d14, c12, s2]) #  3 of a kind

high_card1 = h.PokerHand([c4, c11, s12, c9, c2])
high_card2 = h.PokerHand([s2, c3, s5, c7, s14])
high_card3 = h.PokerHand([c2, s3, c5, s7, s8])
high_card4 = h.PokerHand([s14, s13, c5, c6, c7])
high_card5 = h.PokerHand([c14, c11, s4, s6, s10])
high_card6 = h.PokerHand([s14, s11, c4, c6, c10]) # high card ace


a = h.PokerHand([])

if __name__ == "__main__":
    test_suite = t.create()

    print("Flush Tests:")
    print('')
    t.assert_equals(test_suite, "(f1) If both hands flush, winner has high card", 1, flush1.compare_to(flush2))
    t.assert_equals(test_suite, "(f2) If one hand is flush, other is high card, winner is flush", 1, flush1.compare_to(high_card1))
    t.assert_equals(test_suite, "(f3) If one hand is flush, other is two pair, winner is flush", 1, flush1.compare_to(two_pair1))
    t.assert_equals(test_suite, "(f4) If both hands are flush and exactly the same/equal, tie", 0, flush2.compare_to(flush3))
    print("Two Pair Tests:")
    print('')
    t.assert_equals(test_suite, "(t1) If both hands two pair, winner has higher value pair", 1,two_pair2.compare_to(two_pair3))
    t.assert_equals(test_suite, "(t2) If both hands two pair, and both pairs are same ranks, winner has high card", -1, two_pair1.compare_to(two_pair2))
    t.assert_equals(test_suite, "(t3) If both hands two pair, and both highest pairs are equal, winner has higher value second pair", 1, two_pair3.compare_to(two_pair4))
    t.assert_equals(test_suite, "(t4) If one hand two pair, and other is pair, winner has two pair", 1, two_pair4.compare_to(pair1))
    t.assert_equals(test_suite, "(t5) If one hand two pair, and other is high card, winner has two pair", 1, two_pair4.compare_to(high_card1))
    t.assert_equals(test_suite, "(t6) If one hand two pair (Q, 10) and other is high card (ace), winner is two pair", 1, two_pair6.compare_to(high_card6))
    t.assert_equals(test_suite, "(t7)If one hand is two pair, other is 3 of a kind, two pair wins", -1, pair5.compare_to(two_pair5))
    t.assert_equals(test_suite, "(t8) If both hands are two pair and exactly the same/equal, tie", 0, two_pair4.compare_to(two_pair5))
    print("Pair Tests:")
    print('')
    t.assert_equals(test_suite, "(p1) If both hands pair, winner has pair with higher rank ", 1, pair1.compare_to(pair2))
    t.assert_equals(test_suite, "(p2) If both hands same pair, winner has high card", 1, pair2.compare_to(pair3))
    t.assert_equals(test_suite, "(p3) If one hand pair, other is high card, winner has pair", -1, high_card1.compare_to(pair3))
    t.assert_equals(test_suite, "(p4) If one hand pair, other is high card, winner has pair", 1, pair2.compare_to(high_card6))
    t.assert_equals(test_suite, "(p5) If both hands are pair and exactly the same/equal, tie", 0, pair3.compare_to(pair4))
    print("High Card Tests:")
    print('')
    t.assert_equals(test_suite, "(h1) If both hands have all same ranks except one, winner has high card", 1, high_card2.compare_to(high_card3))
    t.assert_equals(test_suite, "(h2) If all ranks are different, winner has high card", -1, high_card1.compare_to(high_card2))
    t.assert_equals(test_suite, "(h3) If both hands have same high card, winner has next highest card", 1, high_card4.compare_to(high_card5))
    t.assert_equals(test_suite, "(h4) If both hands are high card and exactly the same.equal, tie", 0, high_card5.compare_to(high_card6))
    print('')
    print("Total tests: ", t.num_tests(test_suite))
    print("Fails: ", t.num_fails(test_suite))
    print("Passes:", t.num_passes(test_suite))
    t.print_summary(test_suite)





