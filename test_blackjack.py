import pytest
import blackjack

def test_print_cards():
    testing_card_1 = blackjack.Card((chr(9829), 2), 2)
    testing_card_2 = blackjack.Card((chr(9830), 'Q'), 10)
    assert blackjack.print_cards([testing_card_1, testing_card_2]) == ' ___   ___  \n|2  | |Q  | \n| ♥ | | ♦ | \n|__2| |__Q| \n'
    assert blackjack.print_cards([testing_card_2, testing_card_1]) == ' ___   ___  \n|Q  | |2  | \n| ♦ | | ♥ | \n|__Q| |__2| \n'
    #TODO error checking