import argparse, time, blackjack

STARTING_CARDS = 2
DEFAULT_MONEY = 1000

def main():
    parser = argparse.ArgumentParser(prog='blackjack', description='A gambling game')
    parser.add_argument('-m', '--money', default=DEFAULT_MONEY, help='player\'s (and dealer)\'s starting money', type=int)
    args = parser.parse_args()
    money = args.money

    # TODO Change this
    print('Welcome to Blackjack')
    print('Try to get as close to 21 points as possible without going over.')
    print('Kings, Queens, Jacks are worth as 10 points.')
    print('Number cards (2 through 10) are worth their numeric value.')
    print('Aces can be worth either 1 point or 11 points, depending on which helps your hand more.')
    print('''ACTIONS:
    (H)it: Draw another card to add to your total.
    (S)tand: Keep your current hand and end your turn.
    (D)ouble Down: On your first turn, you can double your initial bet, but you must draw exactly one more card before standing.
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

        print(f"MONEY: ${player.money}\n")

        players = {'player': player, 'dealer': dealer}
        bet = get_bet(player.money)
        if bet == -1:
            print(f"You're bringing ${player.money}.")
            break
        for p in players:
            players[p].bet = bet
            players[p].turn = True
            print(print_stats({'player': player, 'dealer': dealer}))
            while players[p].turn:
                print(f"{p.upper()} TURNS:")
                time.sleep(0.5)
                players[p].get_action()
                time.sleep(0.5)
                print(print_stats({'player': player, 'dealer': dealer}))
                
                if players[p].total_points > blackjack.POINTS:
                    players[p].stand()
                    players[p].lose = True

        print(finishing_game(players))
        if player.money <= 0:
            print("You ran out of money to bet!")
            break
        game += 1

    print("Thank you for playing!")


def print_cards(cards):
    if not cards:
        return ''
    elif len(cards) == 1:
        return str(cards[0])
    s = ''
    card1 = str(cards[0]).split('\n')
    card2 = print_cards(cards[1:]).split('\n')
    for i in range(len(card1)):
        s += card1[i] + card2[i] + '\n'
    return s


def print_stats(players):
    s = ''
    for player in players:
        s += f"{player.upper()}: {players[player].total_points}\n"
        s += f"{print_cards(players[player].cards)}\n"
    return s

def get_bet(max: int) -> int:
    while True:
        bet = input('How much do you want to bet? (Q to quit)\n> ')
        if bet.upper() == 'Q':
            return -1
        try:
            bet = int(bet)
        except ValueError:
            print("Invalid")
        else:
            if bet > 0 and bet <= max:
                return bet
            print("Not enough money")
            

def find_loser(players):
    if players['player'].total_points == players['dealer'].total_points or players['player'].lose == True and players['dealer'].lose == True:
        return -1
    for p in players:
        if players[p].lose:
            return 0
    loser = min(players, key=lambda p: players[p].total_points)
    players[loser].lose = True
    return 0


def finishing_game(players):
    if find_loser(players) == -1:
        return "DRAW"
    else:
        # for p in players:
        #     if players[p].lose:
        #         if p != 'dealer':
        #             players[p].money -= players[p].bet
        #     else:
        #         if p != 'dealer':
        #             players[p].money += players[p].bet
        #         return f'WINNER: {p.capitalize()}'
        if players['player'].lose:
            players['player'].money -= players['player'].bet
            return f'WINNER: Dealer'
        elif players['dealer'].lose:
            players['player'].money += players['player'].bet
            return f'WINNER: Player'


if __name__ == "__main__":
    main()