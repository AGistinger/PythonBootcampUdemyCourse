class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def show_one(self):
        print(f"Dealer is showing {self.all_cards[0]}")

    def card_total(self):
        card_value = 0
        for card in self.all_cards:
            card_value += card.value
        return card_value

    def print_cards(self):
        cards = ""
        for card in self.all_cards:
            cards += f"{card}, "
        return cards

    def __str__(self):
        return f"Dealer Cards: {self.print_cards()}, Value: {self.card_total()}"


if __name__ == "__main__":
    new_dealer = Dealer()
    new_dealer.add_cards(["a", "b", "c"])
    new_dealer.remove_one()
    print(new_dealer)
    print(new_dealer.all_cards)
    new_dealer.show_one()
else:
    print("Player class is imported")
