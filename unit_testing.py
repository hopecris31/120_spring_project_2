import testing_suite as t
import poker_hand as h









if __name__ == "__main__":
    test_suite = t.create()

    print("Flush Tests:")
    t.assert_equals(test_suite, "If both hands flush, winner has high card", expected, actual)
    t.assert_equals(test_suite, "If one hand is flush, other is high card, winner is flush", expected, actual)
    t.assert_equals(test_suite, "If one hand is flush, other is two pair, winner is flush", expected, actual)
    t.assert_equals(test_suite, "If both hands are flush and exactly the same/equal, tie", expected, actual)
    print("Two Pair Tests:")
    t.assert_equals(test_suite, "If both hands two pair, winner has higher value pair", expected, actual)
    t.assert_equals(test_suite, "If both hands two pair, and both pairs are same ranks, winner has high card", expected, actual)
    t.assert_equals(test_suite, "If both hands two pair, and both highest pairs are equal, winner has higher value second pair", expected, actual)
    t.assert_equals(test_suite, "If one hand two pair, and other is pair, winner has two pair", expected, actual)
    t.assert_equals(test_suite, "If one hand two pair, and other is high card, winner has two pair", expected, actual)
    t.assert_equals(test_suite, "If both hands are two pair and exactly the same/equal, tie", expected, actual)
    print("Pair Tests:")
    t.assert_equals(test_suite, "If both hands pair, winner has pair with higher rank ", expected, actual)
    t.assert_equals(test_suite, "If both hands same pair, winner has high card", expected, actual)
    t.assert_equals(test_suite, "If one hand pair, other is high card, winner has pair", expected, actual)
    t.assert_equals(test_suite, "If both hands are pair and exactly the same/equal, tie", expected, actual)
    print("High Card Tests:")
    t.assert_equals(test_suite, "If both hands have all same ranks except one, winner has high card", expected, actual)
    t.assert_equals(test_suite, "If all ranks are different, winner has high card", expected, actual)
    t.assert_equals(test_suite, "If both hands have same high card, winner has next highest card", expected, actual)
    t.assert_equals(test_suite, "If both hands are high card and exactly the same.equal, tie", expected, actual)
    print("Total tests: ", t.num_tests(test_suite))
    print("Fails: ", t.num_fails(test_suite))
    print("Passes:", t.num_passes(test_suite))
    t.print_summary()





