import random

from deck.card import Card

SUITS = ["club", "diamond", "heart", "spade"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Deck:
    def __init__(self):
        self.cards = []
        self.deck_size = 0

    def shuffle(self) -> Deck:
        random.shuffle(self.cards)
        return self

    def clear(self) -> Deck:
        self.cards = []
        return self

    def create(self, num_decks: int) -> Deck:
        for _ in range(num_decks):
            self.__add_cards()
        self.deck_size = len(self.cards)
        return self        

    def __add_cards(self):
        cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(rank, suit)
                cards.append(card)
        self.cards.extend(cards)
