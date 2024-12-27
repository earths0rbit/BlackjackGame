from card import Card

class Deck:
    def __init__(self, num_decks=1):
        """Initialize the deck with the specified number of decks"""
        self.num_decks = num_decks
        self.cards = self._build_deck()

    def _build_deck(self):
        """Builds a single or multiple decks of cards."""
        suits = {'spades': '♠️', 'hearts': '♥️', 'diamonds': '♦️', 'clubs': '♣️'}
        card_values = {
            'ace': 'A', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
            'ten': '10', 'jack': 'J', 'queen': 'Q', 'king': 'K'
        }

        deck = []
        for _ in range(self.num_decks):
            for value in card_values.values():
                for suit in suits.values():
                    deck.append(Card(value, suit))
        return deck
    
    def shuffle(self):
        """Shuffle the deck"""
        import random
        random.shuffle(self.cards)
        random.shuffle(self.cards)

    def deal_card(self):
        """Deal one card fromm the deck."""
        if self.cards:
            return self.cards.pop(0)
        else:
            raise ValueError("The deck is empty!")
        
    def cards_left(self):
        """Returns the number of cards in the deck"""
        return len(self.cards)
    
    