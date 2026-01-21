from deck.deck import Deck
from player.player import Player

class GameManager:
    def __init__(self, num_players: int = 1, num_decks: int = 1):
        #self.players = self.create_players(self.__num_players)
        self.deck = self.__create_deck(num_decks)

        for card in self.deck.cards:
            print(card)

    def __create_players(self, num_players: int) -> list[Player]:
        pass

    def __create_deck(self, num_decks: int) -> Deck:
        deck = Deck()
        deck.create(num_decks)
        #deck.shuffle()
        return deck