from deck import Deck
from player import Player
from dealer import Dealer

class Game:
    def __init__(self):
        """Initializes the game components"""
        self.players = []
        self.dealer = Dealer()
        self.deck = None
        self.num_players = 0

    def setup_game(self):
        """Prompt user for inputs and setup the game."""
        # prompt for number of players
        while True:
            try:
                self.num_players = int(input("How many players? (1-7): "))
                if 1 <= self.num_players <= 7:
                    break
                else:
                    print("Please choose a number between 1 and 7.")
            except ValueError:
                print("Please enter a valid number.")

        # prompt for number of decks
        while True:
            try:
                num_decks = int(input("How many decks? (1, 2, 6, 8): "))
                if num_decks in [1, 2, 6, 8]:
                    self.deck = Deck(num_decks)
                    self.deck.shuffle()
                    break
                else:
                    print("Please choose 1, 2, 6, or 8 decks.")
            except ValueError:
                print("Please enter a valid number.")

        # initialize the players
        self.players = [Player(f"Player {i+1}") for i in range(self.num_players)]

    def deal_initial_cards(self):
        """Deal two cards to each player and the dealer."""
        for _ in range(2):
            for player in self.players:
                player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

        # Display player hands
        for player in self.players:
            print(f"{player.name}'s hand: {player.show_hand()} (Value: {player.calculate_hand()})")

        # Display dealer's hand with one card hidden
        print(f"Dealer's hand: {self.dealer.show_hand(hide_first_card=True)}")

        
    def start_game(self):
        """Start and control the game flow."""
        self.setup_game()
        self.deal_initial_cards()
        # Placeholder for additional game logic (player actions, dealer logic, results)
        print("\nGame setup complete. Ready for the next steps!")






