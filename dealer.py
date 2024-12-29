from player import Player

class Dealer(Player):
    def __init__(self):
        super().__init__(name="Dealer")

    def should_hit(self):
        """Determine if the dealer should hit based on blackjack rules."""
        return self.calculate_hand() < 17
    
    
