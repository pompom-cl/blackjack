import pytest, project, blackjack

decks = blackjack.Deck.generate_deck()
player = blackjack.Player(100)
dealer = blackjack.Dealer(None)

def test_print_cards():
    testing_card_1 = blackjack.Card((chr(9829), 2), 2)
    testing_card_2 = blackjack.Card((chr(9830), 'Q'), 10)
    assert project.print_cards([testing_card_1, testing_card_2]) == ' ___   ___  \n|2  | |Q  | \n| ♥ | | ♦ | \n|__2| |__Q| \n'
    assert project.print_cards([testing_card_2, testing_card_1]) == ' ___   ___  \n|Q  | |2  | \n| ♦ | | ♥ | \n|__Q| |__2| \n'

def test_print_stats():
    assert project.print_stats({'dealer': dealer, 'player': player}) == 'DEALER: 0\n\nPLAYER: 0\n\n'
    player.hit()
    assert project.print_stats({'dealer': dealer, 'player': player}) == 'DEALER: 0\n\nPLAYER: 2\n ___  \n|2  | \n| ♥ | \n|__2| \n'
    dealer.hit()
    assert project.print_stats({'dealer': dealer, 'player': player}) == 'DEALER: 2\n ___  \n|2  | \n| ♦ | \n|__2| \nPLAYER: 2\n ___  \n|2  | \n| ♥ | \n|__2| \n'
    

def test_get_bet(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '50')
    assert project.get_bet(100) == 50
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert project.get_bet(100) == 1
    monkeypatch.setattr('builtins.input', lambda _: '100')
    assert project.get_bet(100) == 100
    monkeypatch.setattr('builtins.input', lambda _: '100100100100')
    assert project.get_bet(100100100100) == 100100100100
    monkeypatch.setattr('builtins.input', lambda _: 'q')
    assert project.get_bet(100) == -1
    monkeypatch.setattr('builtins.input', lambda _: 'Q')
    assert project.get_bet(100) == -1


def test_find_loser():
    reset_stats()
    assert player.total_points == 2
    assert dealer.total_points == 2
    assert project.find_loser({'dealer': dealer, 'player': player}) == -1
    assert player.lose is False
    assert dealer.lose is False
    
    reset_stats()
    player.hit()
    assert player.total_points == 4
    assert dealer.total_points == 2
    project.find_loser({'dealer': dealer, 'player': player})
    assert player.lose is False
    assert dealer.lose is True
    
    reset_stats()
    dealer.hit()
    assert player.total_points == 4
    assert dealer.total_points == 4
    assert project.find_loser({'dealer': dealer, 'player': player}) == -1
    assert player.lose is False
    assert dealer.lose is False
    
    reset_stats()
    dealer.hit()
    assert player.total_points == 4
    assert dealer.total_points == 7
    project.find_loser({'dealer': dealer, 'player': player})
    assert player.lose is True
    assert dealer.lose is False


def test_finishing_game():
    reset_stats()
    player.bet = 10
    assert player.total_points == 4
    assert dealer.total_points == 7
    assert project.finishing_game({'dealer': dealer, 'player': player}) == 'WINNER: Dealer'
    assert player.lose is True
    assert dealer.lose is False
    assert player.money == 90

    reset_stats()
    player.hit()
    assert player.total_points == 7
    assert dealer.total_points == 7
    assert project.finishing_game({'dealer': dealer, 'player': player}) == 'DRAW'
    assert player.money == 90

    
    reset_stats()
    player.bet = 110
    player.hit()
    player.hit()
    player.hit()
    player.hit()
    assert player.total_points == 21
    assert dealer.total_points == 7
    assert project.finishing_game({'dealer': dealer, 'player': player}) == 'WINNER: Player'
    assert player.money == 200




def reset_stats():
    player.lose = False
    dealer.lose = False
