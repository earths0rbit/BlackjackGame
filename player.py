class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        """Add a card to the palyer's hand."""
        self.hand.append(card)

    def reset_hand(self):
        """Reset the player's hand."""
        self.hand = []

    def calculate_hand(self):
        """Calculate the value of the player's hand."""
        value = 0
        aces = 0

        for card in self.hand:
            card_value = card.value
            if card_value in ["J", "Q", "K"]:
                value += 10
            elif card_value == "A":
                aces += 1
                value += 11
            else:
                value += int(card_value)

        # adjust for aces if value is greater than 21
        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value 
    
    def show_hand(self, hide_first_card=False):
        """Return a string representation of the hand."""
        if hide_first_card:
            return f"{self.hand[0]} 🃏"
        return " ".join(str(card) for card in self.hand)
