import argparse
import random

SUITS = (chr(9829), chr(9830), chr(9824), chr(9827)) # '♥'.'♦'.'♠'.'♣'
RANKS = list(range(2, 11)) + ['J', 'Q', 'K', 'A']

class Deck():
    def __init__(self):
        self.cards = []
        self.removed_cards = []
        for i in range(len(RANKS)):
            for j in range(len(SUITS)):
                point = 0
                if i == 12:
                    point = (1, 11)
                elif i > 9:
                    point = 10
                else:
                    point = i + 2
                self.cards.append(Card((SUITS[j], RANKS[i]), point))

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        self.removed_cards.append(self.cards.pop(0))

    def reset(self):
        self.cards += self.removed_cards
        self.shuffle()
        



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
    def __init__(self):
        self.cards = []
        self.total_points
        self.actions = []
        self.hidden

    def hit(self, deck: Deck):
        self.cards.append(deck.cards[0])
        deck.deal()

    def stand(self):
        ...

    def double(self):
        ...

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
    ... #TODO

class Dealer(Entity):
    def hide(self):
        self.cards[0].hide = True
    ... #TODO


def main():
    parser = argparse.ArgumentParser(prog='blackjack', description='A gambling game')
    parser.add_argument('-m', '--money', default=1000, help='player\'s (and dealer)\'s starting money', type=int)
    args = parser.parse_args()

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
    deck = Deck()
    deck.shuffle()
    player = create_entity(deck)
    dealer = create_entity(deck, dealer=True)

    while True:
        print(f"DEALER: {dealer.total_points}")
        print(print_cards(dealer.cards, hide=1))
        print(f"PLAYER: {player.total_points}")
        print(print_cards(player.cards))
        break


def print_cards(cards, hide: int=0):
    if len(cards) == 1:
        return str(cards[0])
    s = str()
    card1 = str(cards[0]).split('\n')
    card2 = print_cards(cards[1:]).split('\n')
    for i in range(len(card1)):
        s += card1[i] + card2[i] + '\n'
    return s


def create_entity(deck, dealer=False):
    entity = Entity()
    entity.hit(deck)
    entity.hit(deck)
    if dealer:
        entity.cards[0].hide = True
    return entity


if __name__ == "__main__":
    main()
