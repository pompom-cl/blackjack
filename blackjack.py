import random

class Deck():
    suits = (chr(9829), chr(9830), chr(9824), chr(9827))
    ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    def __init__(self):
        self.cards = []
        self.removed_cards = []
        for i in range(len(Deck.ranks)):
            for j in range(len(Deck.suits)):
                point = 0
                if i == 12:
                    point = (1, 11)
                elif i > 9:
                    point = 10
                else:
                    point = i + 2
                self.cards.append(Card((Deck.suits[j], Deck.ranks[i]), point))

    def shuffle(self):
        random.shuffle(self.cards)


class Card():
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
|{str(self.pair[1]).ljust(2)} | 
| {self.pair[0]} | 
|_{str(self.pair[1]).rjust(2, '_')}| '''
    

    


class Entity():
    def __init__(self):
        self.cards = []
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
    deck = Deck()
    # deck.shuffle()
    for card in deck.cards:
        print(card)
    s = print_cards(deck.cards)


def print_cards(cards):
    if len(cards) == 1:
        return str(cards[0])
    s = str()
    card1 = str(cards[0]).split('\n')
    card2 = print_cards(cards[1:]).split('\n')
    for i in range(len(card1)):
        s += card1[i] + card2[i] + '\n'
    return s

    


if __name__ == "__main__":
    main()
