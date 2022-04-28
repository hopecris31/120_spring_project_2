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

#hand1 = h.PokerHand(card_list1)

flush1 = h.PokerHand([c10, c11, c12, c13, c14])  # highest flush hand
flush2 = h.PokerHand([s9, s8, s7, s6, s5, s4])  # second-highest flush hand
flush3 = h.PokerHand([c9, c8, c7, c6, c5, c4])  # same as hand above w different suits

two_pair1 = h.PokerHand([c14, c10, c14, c10, c4])

high_card1 = h.PokerHand([c4, c3, c5, c7, c8])





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
    t.assert_equals(test_suite, "(t1) If both hands two pair, winner has higher value pair", expected, actual)
    t.assert_equals(test_suite, "(t2) If both hands two pair, and both pairs are same ranks, winner has high card", expected, actual)
    t.assert_equals(test_suite, "(t3) If both hands two pair, and both highest pairs are equal, winner has higher value second pair", expected, actual)
    t.assert_equals(test_suite, "(t4) If one hand two pair, and other is pair, winner has two pair", expected, actual)
    t.assert_equals(test_suite, "(t5) If one hand two pair, and other is high card, winner has two pair", expected, actual)
    t.assert_equals(test_suite, "(t6) If both hands are two pair and exactly the same/equal, tie", expected, actual)
    print("Pair Tests:")
    print('')
    t.assert_equals(test_suite, "(p1) If both hands pair, winner has pair with higher rank ", expected, actual)
    t.assert_equals(test_suite, "(p2) If both hands same pair, winner has high card", expected, actual)
    t.assert_equals(test_suite, "(p3) If one hand pair, other is high card, winner has pair", expected, actual)
    t.assert_equals(test_suite, "(p4) If both hands are pair and exactly the same/equal, tie", expected, actual)
    print("High Card Tests:")
    print('')
    t.assert_equals(test_suite, "(h1) If both hands have all same ranks except one, winner has high card", expected, actual)
    t.assert_equals(test_suite, "(h2) If all ranks are different, winner has high card", expected, actual)
    t.assert_equals(test_suite, "(h3) If both hands have same high card, winner has next highest card", expected, actual)
    t.assert_equals(test_suite, "(h4) If both hands are high card and exactly the same.equal, tie", expected, actual)
    print('')
    print("Total tests: ", t.num_tests(test_suite))
    print("Fails: ", t.num_fails(test_suite))
    print("Passes:", t.num_passes(test_suite))
    t.print_summary()





