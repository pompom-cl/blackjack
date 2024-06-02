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

## How to run

1. Make sure you have Python installed.
1. Make sure you have met all of the [requirements](https://github.com/pompom-cl/blackjack/blob/main/requirements.txt)
1. Download or clone the project files.
    ``` sh
    git clone https://github.com/pompom-cl/blackjack.git
    ```
1. Run the game with the command
    ``` sh
    python project.py
    ```
    or with `-m` or `--money` argument for how much money you want to start with. If not specified, the default starting money is $1000.
    ``` sh
    python project.py -m 2000
    ```


## Index
| Filename | Description |
| --- | --- |
| [project.py](https://github.com/pompom-cl/blackjack/blob/main/README.md#projectpy) | Contains main function and other functions, which handles the game loop, player and dealer actions, betting system, and game outcomes. |
| [blackjack.py](https://github.com/pompom-cl/blackjack/blob/main/README.md#blackjackpy) | Contains the abstractions of the Blackjack game, including the Deck, Card, Player, and Dealer classes. |
| [test_project.py](https://github.com/pompom-cl/blackjack/blob/main/README.md#test_projectpy) | Contains all test functions for all functions in `project.py` |
| [requirements.txt](https://github.com/pompom-cl/blackjack/blob/main/README.md#libraries) | Contains all of the required libraries |

### project.py

| Function | Description |
| --- | --- |
| `main()` | Function: Parsing arguments; printing command-line UI; main game loop |
| `print_cards(cards)` | Recursive function to print cards horizontally |
| `print_stats(players)` | Print player's and dealer's total points and hand (by calling print_cards function) |
| `get_bet(max)` | Ask bet (input) from the user |
| `find_loser(players)` | Change player's or dealer's lose attribute accordingly. Return -1 if there's no winner |
| `finishing_game(players)` | Print draw if draw, otherwise, print the winner |

### blackjack.py

#### class Deck()

| Class method | Description |
| --- | --- |
| `generate_deck(cls)` | Generates all cards and add to the stack |
| `shuffle(cls)` | Shuffles cards using random library |
| `deal(cls)` | Adds topmost card to the removed_cards |
| `reset(cls)` | Adds all removed_cards to cards stack, removed all removed_cards, reset card's hide attribute to False, and shuffle the stack |

#### class Card()

| Attribute | Description |
| --- | --- |
| `self.pair` | Tuple to identify the rank and suit |
| `self.point` | Point of the card |
| `self.hide` | The card cannot be seen if this attribute is True |


| Method | Description |
| --- | --- |
| `__init__(self, pair, point)` | Initialization |
| `__str__(self)` | Returns the string representation of the card |

#### class Entity()

| Attribute | Description |
| --- | --- |
| `self.cards` | Entity's hand |
| `self.total_points` | Entity's total points |
| `self.actions` | Entity's actions in one game |
| `self.hidden` | Determines if entity has any hidden cards |
| `self.turn` | Determines entity's turn in game |
| `self.bet` | Entity's bet for the game (player) |
| `self.lose` | Determines if entity is losing |
| `self.money` | Entity's total money |


| Method | Description |
| --- | --- |
| `__init__(self, money)` |  |
| `hit(self)` | Draws a card |
| `stand(self)` | Ends the turn |
| `calculate_points(self)` | Calculates the total points of the entity's hand |

#### class Player(Entity)

| Method | Description |
| --- | --- |
| `new_game(self)` | Resets the player's state for a new game |
| `get_action(self)` | Prompts the player to take an actions |
| `double(self)` | Doubles the bet, draws a card, ends the turn |

#### class Dealer(Entity)

| Method | Description |
| --- | --- |
| `new_game(self)` | Resets the dealer's state for a new game |
| `get_action(self)` | Determines the dealer's action based on the current total_points |
| `unhide(self)` | Unhides the dealer's hidden card |

## About Me

I'm Clara Maria Lie. I'm from Cikarang, Indonesia.
