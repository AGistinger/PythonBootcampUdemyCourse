* For this project you will use OOP to create a
BlackJack Game with Python.
* For our version of the game we will only have a computer
dealer and a human player.
* We start with a normal deck of cards, you will create
a representation of a deck with Python.
* Human player places the bet, has a bankroll
* Player starts with two cards face up
* Dealer starts with one card face up and one face down
* Player goes first
* Player goal: get closer to a total value of 21 than
the dealer does.
* Player possible actions:
    * Hit (receive another card)
    * Stay (stop receiving cards)
* Dealer:
    * Dealer will hit until they beat the player, or they bust
* If the player wins they double their bet, and it goes to
the bankroll
* Special Rules:
    * Face Cards (Jack, Queen, King) count as a value of 10
    * Aces can count as either 1 or 11, whichever value
    is preferable to the player

Game Play:
To play a hand of BlackJack the following steps must be followed:
1. Create a deck of 52 cards
2. Shuffle the deck
3. Ask the player for their bet
4. Make sure that the Player's bet does not exceed their available chips
5. Deal two cards to the Dealer and two cards to the player
6. Show only one of the Dealer's cards, the other remains hidden
7. Show both of the Player's cards
8. Ask the player if they wish to Hit, and take another card
9. If the Player's hand doesn't Bust (go over 21), ask if they'd
like to hit again
10. If the Player Stands, play the Dealer's hand.  The dealer will always hit
until the Dealer's value meets or exceeds 17
11. Determine the winner and adjust the Player's chips accordingly
12. Ask the Player if they would like to play again
