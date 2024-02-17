import argparse
import random
import time

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
            actions['hit'] = 1
            actions['stand'] = 0
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
    player = Player(money)
    dealer = Dealer(None)


    game = 1
    while True:
        Deck.reset()
        player.new_game()
        dealer.new_game()
        print(f"\nGAME {game}")

        print(f"MONEY: {player.money}\n")

        players = {'player': player, 'dealer': dealer}
        bet = get_bet(player.money)
        if bet == None:
            print(f"You brought home {player.money}")
            break
        for p in players:
            players[p].bet = bet
            players[p].turn = True
            print_stats({'player': player, 'dealer': dealer})
            while players[p].turn:
                print(f"{p.upper()} TURNS:")
                time.sleep(0.5)
                players[p].get_action()
                time.sleep(0.5)
                print_stats({'player': player, 'dealer': dealer})
                
                if players[p].total_points > POINTS:
                    players[p].stand()
                    players[p].lose = True

        find_loser(players)
        finishing_game(players, bet)
        if player.money <= 0:
            print("You run out of money to bet!")
            break
        game += 1

    print("Thank You For Playing!")


def print_cards(cards):
    if len(cards) == 1:
        return str(cards[0])
    s = str()
    card1 = str(cards[0]).split('\n')
    card2 = print_cards(cards[1:]).split('\n')
    for i in range(len(card1)):
        s += card1[i] + card2[i] + '\n'
    return s


def create_entity(money, dealer=False):
    entity = Dealer(money) if dealer else Player(money)
    for i in range(STARTING_CARDS):
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
        bet = input('How much do you want to bet? (Q to quit)\n> ')
        if bet.upper() == 'Q':
            return None
        try:
            bet = int(bet)
        except ValueError:
            print("Invalid")
        else:
            if bet > 0 and bet <= max:
                return bet
            print("Not enough money")
            

def find_loser(players):
    for p in players:
        if players[p].lose:
            return None
    
    loser = min(players, key=lambda p: players[p].total_points)
    players[loser].lose = True

def finishing_game(players, bet):
    draw = True
    draw_point = players['dealer']
    for p in players:
        if draw_point != players[p]:
            draw = False
    if draw:
        print("DRAW")
    else:
        for p in players:
            print(players[p].money)
            print(players[p].lose)
            if players[p].lose:
                if p != 'dealer':
                    players[p].money -= players[p].bet
            else:
                if p != 'dealer':
                    players[p].money += players[p].bet
                print(f'WINNER: {p.capitalize()}')



if __name__ == "__main__":
    main()
