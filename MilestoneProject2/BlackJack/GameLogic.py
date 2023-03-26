from BlackJack import Player
from BlackJack import Dealer
from BlackJack import Deck


# Function to Create new player with input from player
def create_player():
    name = ""
    while name == "":
        name = input("Please enter your name:")
    chips = ""
    while not chips.isdigit():
        chips = input("Please enter your amount of chips:")

    chips = int(chips)
    return Player.Player(name, chips)


def hit(player):
    player.add_cards(new_deck.deal_one())


def bust(player):
    if player.card_total() > 21:
        print(f"{player.name} has gone bust Card Total: {player.card_total()}")
        return True
    else:
        return False


player = create_player()
dealer = Dealer.Dealer()

new_deck = Deck.Deck()
new_deck.shuffle_deck()

playing = True

while playing:
    # Get bet
    player.place_bet()

    # Draw first cards
    for draw in range(2):
        player.add_cards(new_deck.deal_one())
        dealer.add_cards(new_deck.deal_one())

    # Show all players cards and one dealer card
    print(player)
    dealer.show_one()

    # Player hit until done
    player_hitting = True
    while player_hitting:
        player_input = ""
        while player_input not in ["H", "S"]:
            player_input = input("Do you want to Hit (H) or Stay (S)?").upper()

        if player_input == "H":
            hit(player)
            print(player)
            player_input = ""

            if bust(player):
                print(f"{dealer.name} Wins!")
                player.lose_bet()
                player_hitting = False
                playing = False
        else:
            player_hitting = False

    # Dealer hitting till beat the player or bust
    dealer_hitting = True
    while dealer_hitting:
        if dealer.card_total() < player.card_total():
            dealer.add_cards(new_deck.deal_one())
            print(dealer)
            if bust(dealer):
                print(f"{player.name} Wins! ${player.current_bet * 2}")
                player.win_bet()
                dealer_hitting = False
                playing = False

    if player.card_total() > dealer.card_total():
        player.win_bet()
        print(f"{player.name} Wins! ${player.current_bet * 2}")
        playing = False
    elif player.card_total() == 21:
        player.win_bet()
        print(f"{player.name} Wins! ${player.current_bet * 2}")
        playing = False
    elif (dealer.card_total() == 21) or (dealer.card_total() < player.card_total()):
        print(f"{dealer.name} Wins!")
        player.lose_bet()
        playing = False
