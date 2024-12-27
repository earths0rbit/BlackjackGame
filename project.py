## blackjack card game

from card import Card
from deck import Deck
import random
import time

# define dictionary for the 4 suits in a standard deck of playing cards
suits = {
    'spades': '♠️',
    'hearts': '♥️',
    'diamonds': '♦️',
    'clubs': '♣️'
}

# define dictionary for the values of the cards in a standard deck of playing cards
cards = {
    'ace': 'A',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'ten': '10',
    'jack': 'J',
    'queen': 'Q',
    'king': 'K',
}

def main():
    """Main is a function that controls the main flow of the game"""
    # Prompts the user for a number of players to play the game
    # error checking for valid number between 1 - 7
    while True:
        try:
            players = int(input("How many players? (1-7) "))
            if 1 <= players <= 7:
                break
            else:
                print("Please choose a number between 1 and 7.")
                continue
        except ValueError as e:
            print("Please enter a valid number.")
   
    # Prompts the user for a number of decks to play the game with
    # error checking for valid number of 1, 2, 6, 8
    while True:
        try:   
            num_decks = int(input("How many decks? (1,2,6,8) "))
            if num_decks in [1, 2, 6, 8]:
                break
            else:
                print("Please choose 1, 2, 6, or 8 decks.")
                continue
        except ValueError as e:
            print("Please enter a valid number.")

    # Create and shuffle the deck
    deck = Deck(num_decks) # Initialize the Deck with the specified number of decks
    deck.shuffle()         # Shuffle the deck

    # Deal cards to players and the dealer
    deal(deck, players)

def build_deck():
    """Builds a single deck of cards using suits and cards"""
    deck = []
    for  value in cards.values():
        for suit in suits.values():
            deck.append(Card(value, suit))
    return deck

def build_shoe(deck, num_decks):
    """Builds a shoe based on deck and how many decks the player chosen"""
    return deck * num_decks # num decks is set via input from the player

def shuffle(cards):
    return random.shuffle(cards)

def deal(deck, players):
    """Simplified logic to deal two cards to each player and the dealer."""
    # Initialize hands for players and dealer
    player_hands = [[] for _ in range(players)]
    dealer_hand = []

    # Deal two cards to each player and the dealer
    for _ in range(2):
        for i in range(players):
            player_hands[i].append(deck.deal_card())
        dealer_hand.append(deck.deal_card())

    # Display each player's hand
    for idx, hand in enumerate(player_hands, start=1):
        hand_value = calculate_hand(hand)
        print(f"Player {idx}'s hand: {' '.join(str(card) for card in hand)} (Value: {hand_value})")

    # Display the dealer's hand
    print(f"Dealer's hand: {dealer_hand[0]} 🃏")

def calculate_hand(hand):
    """Calculates the total value of a hand in blackjack."""
    value = 0
    aces = 0

    for card in hand:
        card_value = card.value
        if card_value in ["J", "Q", "K"]:
            value += 10
        elif card_value == "A":
            aces += 1
            value +=11
        else:
            value += int(card_value)
        
    # calculating if aces
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

if __name__ == "__main__":
    main()