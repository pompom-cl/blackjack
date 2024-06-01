# Blackjack
#### Video Demo:  <URL HERE>
#### Description: Simple implementation of a command-line Blackjack game.

## What is this?
my cs50p final project's repository.

This project is a simple implementation of a command-line Blackjack game, where the player competes against the dealer to get as close to 21 points as possible without going over.

### Rules:
- Try to get as close to 21 points as possible without going over.
- Kings, Queens, Jacks are worth as 10 points.
- Number cards (2 through 10) are worth their numeric value.
- Aces can be worth either 1 point or 11 points, depending on which helps your hand more.

### Actions:
- (H)it: Draw another card to add to your total.
- (S)tand: Keep your current hand and end your turn.
- (D)ouble Down: On your first turn, you can double your initial bet, but you must draw exactly one more card before standing.


## Libraries

- argparse ([docs](https://docs.python.org/3/library/argparse.html)) for parsing command-line arguments
- random [docs](https://docs.python.org/3/library/random.html)
- time [docs](https://docs.python.org/3/library/time.html)


## Index
| Filename | Description |
| --- | --- |
| [project.py](https://github.com/pompom-cl/blackjack/blob/main/README.md#projectpy) | Contains main function and other functions, which handles the game loop, player and dealer actions, betting system, and game outcomes. |
| `blackjack.py` | Contains the abstractions of the Blackjack game, including the Deck, Card, Player, and Dealer classes. |
| `test_project.py` | Contains all test functions for all functions in `project.py` |
| `requirements.txt` | Contains all of the required libraries |

### project.py

| Function | Description |
| --- | --- |
| `main()` |  |
| `print_cards(cards)` |  |
| `print_stats(players)` |  |
| `get_bet(max)` |  |
| `find_loser(players)` |  |
| `finishing_game(players)` |  |

### blackjack.py

#### class Deck()

| Class method | Description |
| --- | --- |
| `generate_deck(cls)` |  |
| `shuffle(cls)` |  |
| `deal(cls)` |  |
| `reset(cls)` |  |

#### class Card()

| Attribute | Description |
| --- | --- |
| `self.pair` |  |
| `self.point` |  |
| `self.hide` |  |


| Method | Description |
| --- | --- |
| `__init__(self, pair, point)` |  |
| `__str__(self)` |  |

#### class Entity()

| Attribute | Description |
| --- | --- |
| `self.cards` |  |
| `self.total_points` |  |
| `self.actions` |  |
| `self.hidden` |  |
| `self.turn` |  |
| `self.bet` |  |
| `self.lose` |  |
| `self.money` |  |


| Method | Description |
| --- | --- |
| `__init__(self, money)` |  |
| `hit(self)` |  |
| `stand(self)` |  |
| `calculate_points(self)` |  |

#### class Player(Entity)

| Method | Description |
| --- | --- |
| `new_game(self)` |  |
| `get_action(self)` |  |
| `double(self)` |  |

#### class Dealer(Entity)

| Method | Description |
| --- | --- |
| `new_game(self)` |  |
| `get_action(self)` |  |
| `unhide(self)` |  |

## About Me

I'm Clara Maria Lie. I'm from Cikarang, Indonesia.
