## blackjack card game

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

    shoe = build_shoe(build_deck(), num_decks)
    shuffle(shoe)
    deal(shoe, players)


def build_deck():
    """Builds a single deck of cards using suits and cards"""
    deck = []
    for card_value in cards.values():
        for suit_symbol in suits.values():
            deck.append(card_value + suit_symbol)
    return deck

def build_shoe(deck, num_decks):
    """Builds a shoe based on deck and how many decks the player chosen"""
    return deck * num_decks # num decks is set via input from the player

def shuffle(cards):
    return random.shuffle(cards)

def deal(shoe, players):
    # empty list with logic to build empty lists to hold players hands depending on how many players
    player_hands = [[] for _ in range(players)]

    # empty lsit for the dealer's hand
    dealer_hand = []

    # dealers face down card as to not display it when hand is dealt
    dealer_hidden_card = None
    
    # empty list for the cards already played in a shoe / deck
    # discard pile is also used in testing to print cards already used to check that logic is behavng as expected
    discard_pile = []
    
    """Logic to deal the cards to the players in turn from player 1 - (2-7) then dealer.
    Dealers second card gets dealt face down and the actual card is placed in a list called dealer_hidden_card"""
    for i in range(2):
        for j in range(players): # num players is set via input from the player
            card = shoe.pop(0)
            discard_pile.append(card)
            player_hands[j].append(card)
            print(f"Player {j + 1} gets a {card}")
            time.sleep(1)
        dealer_card = shoe.pop(0)
        discard_pile.append(dealer_card)
        if i == 0:
            dealer_hand.append(dealer_card)
            print(f"Dealer gets a {dealer_card}")
            time.sleep(1)
        else:
            dealer_hidden_card = dealer_card
            dealer_hand.append("🃏")
            print("Dealer gets a 🃏")
    for idx, hand in enumerate(player_hands, start=1):
        hand_value = calculate_hand(hand)
        print(f"Player {idx}'s hand: {' '.join(hand)} (Value: {hand_value})")
        time.sleep(1)
    
    dealer_hand_value = calculate_hand([dealer_hand[0]])
    print(f"Dealers hand: {dealer_hand[0]} 🃏 (Showing: {dealer_hand_value})")
    # print(f"\nRemaining shoe cards: {len(shoe)}\n{shoe}")
    # print(f"\nDiscard pile: {len(discard_pile)}\n{discard_pile}")



    ### SAVE FOR LATER  ###
    #  Revealing dealers hand and value 
    """ dealer_hand[1] = dealer_hidden_card
    print(f"Dealer has: {' '.join(dealer_hand)} (Value: {calculate_hand(dealer_hand)})") """

def calculate_hand(hand):
    value = 0
    aces = 0

    for card in hand:
        card_value = card[:-2]
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