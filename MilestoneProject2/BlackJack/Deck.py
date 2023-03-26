from BlackJack import Card
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

    def deal(self):
        if len(self.all_cards) >= 2:
            card_one = self.all_cards.pop()
            card_two = self.all_cards.pop()
            return [card_one, card_two]
        else:
            print("Not enough cards available in Deck")

    def deal_one(self):
        if len(self.all_cards) > 0:
            return self.all_cards.pop()
        else:
            print("No more cards available in Deck")

    def __str__(self):
        deck_comp = ""
        for card in self.all_cards:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp


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
