"""
Game "war"
52 card deck that is split up into 2 decks.
Each player will put a card on the table.
Card with higher ranking wins.
Winner takes both cards and puts them in the deck.
Loser is the one with no cards are remaining.
If cards are the same value (war):
In a war situation another set of cards is taken out.
Then they draw again, then the winner takes all the sets
of cards.
The playing of the game will occur with two virtual agents
not players.

The game will require:
    * Card Class
    * Deck Class
    * Player Class
    * Game Logic
"""
# Global Variables
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
         "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
          "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11,
          "Queen": 12, "King": 13, "Ace": 14}


class Card:

    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suite
