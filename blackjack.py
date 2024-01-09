import random

class Deck():
    suits = (chr(9829), chr(9830), chr(9824), chr(9827))
    ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    def __init__(self, cards):
        self.cards = cards
    @classmethod
    def generate_deck(cls):
        cards = []
        for i in range(len(cls.ranks)):
            for j in range(len(cls.suits)):
                point = 0
                match i:
                    case 12:
                        point = (1, 11)
                        
                    case_:
                        cards.append(Card((cls.ranks[i], cls.suits[j]), i + 2))


class Card():
    played_deck = []
    suits = (chr(9829), chr(9830), chr(9824), chr(9827))
    ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']

    @classmethod
    def generate_random(cls, n=1):
        cards = []
        for i in range(n):
            while True:
                try:
                    cards.append(Card((random.choice(cls.suits), random.choice(cls.ranks))))
                except ValueError:
                    pass
                else:
                    break
        return cards if n > 1 else cards[0]
    
    def __init__(self, pair, point):
        self.pair = pair
        self.point = point
    def __str__(self, hide=False):
        if hide:
             return f''' ___  
|## | 
|###| 
|_##| '''
        return f''' ___  
|{str(self.pair[0]).ljust(2)} | 
| {self.pair[1]} | 
|_{str(self.pair[0]).rjust(2, '_')}| '''
    
    @property
    def pair(self):
        return self._pair
    
    @pair.setter
    def pair(self, pair):
        if pair not in Card.played_deck:
            Card.played_deck.append(pair)
            self._pair = pair
        else:
            raise ValueError('duplicates found')


    


class Entity():
    def __init__(self):
        self.cards = []
        self.points =
    def hit(self, card: Card):
        self.cards.append(card)
    def stand(self):
        ...

def main():
    print('Blackjack, by Al Sweigart al@inventwithpython.com')
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
        The dealer stops hitting at 17.''')
    player = Entity()
    player.hit(Card.generate_random())
    print(player.cards[0])

if __name__ == "__main__":
    main()
