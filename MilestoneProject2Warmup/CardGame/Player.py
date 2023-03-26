"""
Player Class
This class will be used to hold a player's current list of cards
A player should be able to add or remove cards from their "hand"
(list of Card objects).

We will want the player to be able to add a single card or
multiple cards to their list, so we will also explore how
to do this in one method call.

The last thing we need to think about is translating a
Deck/Hand of cards with a top and bottom, to a Python list.
"""


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} card(s)"


if __name__ == "__main__":
    new_player = Player("Jose")
    new_player.add_cards(["a", "b", "c"])
    new_player.remove_one()
    print(new_player)
    print(new_player.all_cards)
else:
    print("Player class is imported")
