import random

SUITS = (chr(9829), chr(9830), chr(9824), chr(9827)) # '♥'.'♦'.'♠'.'♣'
RANKS = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
STARTING_CARDS = 2
POINTS = 21

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
                elif i > 8:
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
        for card in cls.cards:
            card.hide = False
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
        self.turn = False
        self.bet = 0
        self.lose = False
        self.money = money

    def hit(self):
        self.actions.append('hit')
        self.cards.append(Deck.cards[0])
        Deck.deal()

    def stand(self):
        self.actions.append('stand')
        self.turn = False

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
        return max_point if max_point < POINTS else min(points)
    
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
    def new_game(self):
        self.lose = False
        self.actions = []
        self.cards = []
        for i in range(STARTING_CARDS):
            self.hit()

    def get_action(self):
        while True:
            print(f'BET: {self.bet}\n(H)it, (S)tand, (D)ouble down') if len(self.actions) == STARTING_CARDS else print('(H)it, (S)tand')
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
                    if len(self.actions) == STARTING_CARDS:
                        self.double()
                        break
                    print("Cannot do double!")
                case _:
                    print("Invalid action!")


    def double(self):
        self.bet *= 2
        self.hit()
        self.stand()

class Dealer(Entity):
    def new_game(self):
        self.lose = False
        self.actions = []
        self.cards = []
        for i in range(STARTING_CARDS):
            self.hit()
        self.cards[0].hide = True

    def get_action(self):
        self.unhide()
        actions = {}
        point_1 = 11 # hit
        point_2 = random.randint(14, 15)
        point_3 = random.randint(18, 19)
        
        if self.total_points < point_1:
            actions['hit'] = 0.99
            actions['stand'] = 0.09
        elif self.total_points < point_2:
            actions['hit'] = 0.63
            actions['stand'] = 0.37
        elif self.total_points < point_3:
            actions['hit'] = 0.27
            actions['stand'] = 0.73
        else:
            actions['hit'] = 0.09
            actions['stand'] = 0.99
        action = random.choices(list(actions.keys()), list(actions.values()), k=1)[0]
        print(action)
        match action:
            case 'hit':
                self.hit()
            case 'stand':
                self.stand()

    def unhide(self):
        self.cards[0].hide = False if self.cards[0].hide else False

