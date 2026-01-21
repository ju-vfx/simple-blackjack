from deck.card import Card

class Player:
    def __init__(self, start_credits: int = 1000):
        self.hand = []
        self.credits = 0

    def add_card(self, card: Card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

class Dealer(Player):
    def __init__(self):
        super().__init__()
        pass