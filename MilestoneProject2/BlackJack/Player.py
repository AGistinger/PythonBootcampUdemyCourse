class Player:

    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.all_cards = []
        self.current_bet = 0

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def place_bet(self):

        valid_bet = False
        while not valid_bet:
            amount = ""
            while not amount.isdigit():
                amount = input("Please enter a bet amount: ")

            amount = int(amount)
            if amount <= self.chips:
                self.chips -= amount
                self.current_bet = amount
                valid_bet = True
            else:
                print(f"You do not have enough chips to make that bet, Current Chips: {self.chips}")
                amount = ""
                valid_bet = False

    def win_bet(self):
        self.chips += (self.current_bet * 2)
        self.current_bet = 0

    def lose_bet(self):
        self.current_bet = 0

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
        return f"Player: {self.name}, Chips: {self.chips}, Cards: {self.print_cards()}, Value: {self.card_total()}"


if __name__ == "__main__":
    new_player = Player("Jose", 100)
    new_player.add_cards(["a", "b", "c"])
    new_player.remove_one()
    print(new_player)
    print(new_player.all_cards)
else:
    print("Player class is imported")
