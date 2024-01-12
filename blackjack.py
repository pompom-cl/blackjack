import argparse
import random
import sys

SUITS = (chr(9829), chr(9830), chr(9824), chr(9827)) # '♥'.'♦'.'♠'.'♣'
RANKS = list(range(2, 11)) + ['J', 'Q', 'K', 'A']

class Deck():
    cards = []
    removed_cards = []

    @classmethod
    def generate_deck(cls):
        for i in range(len(RANKS)):
            for j in range(len(SUITS)):
                point = 0
                if i == 12:
                    point = (1, 11)
                elif i > 9:
                    point = 10
                else:
                    point = i + 2
                cls.cards.append(Card((SUITS[j], RANKS[i]), point))

    @classmethod
    def shuffle(cls):
        random.shuffle(cls.cards)
        
    @classmethod
    def deal(cls):
        cls.removed_cards.append(cls.cards.pop(0))
        
    @classmethod
    def reset(cls):
        cls.cards += cls.removed_cards
        cls.shuffle()
        

class Card():
    def __init__(self, pair: tuple, point):
        self.pair = pair
        self.point = point
        self.hide = False
    def __str__(self):
        if self.hide:
             return f''' ___  
|## | 
|###| 
|_##| '''
        return f''' ___  
|{str(self.pair[1]).ljust(2)} | 
| {self.pair[0]} | 
|_{str(self.pair[1]).rjust(2, '_')}| '''
    
    @property
    def pair(self):
        return self._pair
    
    @pair.setter
    def pair(self, pair):
        if pair[0] in SUITS and pair[1] in RANKS:
            self._pair = pair
        else:
            raise ValueError("Invalid Card")


class Entity():
    def __init__(self, money):
        self.cards = []
        self.total_points
        self.actions = []
        self.hidden
        self.money = money
        self.winning = False
        self.turn = False

    def hit(self):
        self.actions.append('hit')
        self.cards.append(Deck.cards[0])
        Deck.deal()

    def stand(self):
        self.actions.append('stand')
        self.turn = False


    def double(self):
        self.actions.append('double')

    def calculate_points(self):
        points = []
        for n in range(2):
            points.append(0)
            for i in range(len(self.cards)):
                if self.cards[i].pair[1] == 'A':
                    points[n] += 1 if n == 0 else 11
                else:
                    points[n] += self.cards[i].point
        max_point =max(points) 
        return max_point if max_point < 21 else min(points)
    
    @property
    def total_points(self):
        if self.hidden:
            return '??'
        return self.calculate_points()
    
    @property
    def hidden(self):
        for card in self.cards:
            if card.hide:
                return True
        return False
    
            

class Player(Entity):
    def get_action(self, players):
        while True:
            action = input('> ').strip().lower()
            print()
            match action:
                case 'h':
                    self.hit()
                    break
                case 's':
                    self.stand()
                    break
                case 'd':
                    self.double()
                    break
                case _:
                    pass

class Dealer(Entity):
    ...


def main():
    parser = argparse.ArgumentParser(prog='blackjack', description='A gambling game')
    parser.add_argument('-m', '--money', default=1000, help='player\'s (and dealer)\'s starting money', type=int)
    args = parser.parse_args()
    money = args.money

    print('Welcome to Blackjack (inspired by Al Sweigart)')
    print('''
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.
    ''')
    Deck.generate_deck()
    # Deck.shuffle()
    player = create_entity(money)
    dealer = create_entity(dealer=True)
    print(f"MONEY: {player.money}")
    bet = get_bet(money)

    players = {'player': player, 'dealer': dealer}
    for p in players:
        players[p].turn = True
        while players[p].turn:
            print_stats({'player': player, 'dealer': dealer})
            print('\n(H)it, (S)tand, (D)ouble down')
            players[p].get_action(players)
        
            if players[p].total_points > 21:
                break
    


def print_cards(cards):
    if len(cards) == 1:
        return str(cards[0])
    s = str()
    card1 = str(cards[0]).split('\n')
    card2 = print_cards(cards[1:]).split('\n')
    for i in range(len(card1)):
        s += card1[i] + card2[i] + '\n'
    return s


def create_entity(money=0, dealer=False):
    entity = Entity(None) if dealer else Player(money)
    entity.hit()
    entity.hit()
    if dealer:
        entity.cards[0].hide = True
    return entity

def print_stats(players):
    for player in players:
        print(f"{player.upper()}: {players[player].total_points}")
        print(print_cards(players[player].cards))

def get_bet(max: int) -> int:
    while True:
        bet = input('How much do you want to bet?\n> ')
        try:
            bet = int(bet)
        except ValueError:
            pass
        else:
            if bet > 0 and bet <= max:
                return bet


if __name__ == "__main__":
    main()
