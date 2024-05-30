import argparse, time, blackjack

STARTING_CARDS = 2
POINTS = 21

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
    blackjack.Deck.generate_deck()
    player = blackjack.Player(money)
    dealer = blackjack.Dealer(None)


    game = 1
    while True:
        blackjack.Deck.reset()
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
    entity = blackjack.Dealer(money) if dealer else blackjack.Player(money)
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