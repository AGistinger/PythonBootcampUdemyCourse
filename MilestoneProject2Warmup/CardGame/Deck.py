"""
Deck Class
Instantiate a new deck
Hold as a list of card objects
Shuffle a deck through a method call, random library shuffle()
Deal cards from Deck object
Pop method from cards list
"""
from CardGame import Card
import random


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in Card.suits:
            for rank in Card.ranks:
                # Create the Card Object
                created_card = Card.Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        if len(self.all_cards) > 0:
            return self.all_cards.pop()
        else:
            print("No more cards available in Deck")


if __name__ == "__main__":
    new_deck = Deck()
    new_deck.shuffle_deck()
    card = new_deck.deal_one()
    first_card = new_deck.all_cards[0]
    bottom_card = new_deck.all_cards[-1]
    print(first_card)
    print(card)
else:
    print("Deck class is imported")
