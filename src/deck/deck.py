import random

from deck.card import Card
from settings.settings import SUITS, RANKS

class Deck:
    def __init__(self):
        self.cards = []
        self.deck_size = 0
        self.deck_size_init = 0

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
        self.deck_size_init = self.deck_size
        return self

    def draw(self) -> Card:
        self.deck_size -= 1
        return self.cards.pop(-1)

    def __add_cards(self):
        cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(rank, suit)
                cards.append(card)
        self.cards.extend(cards)
