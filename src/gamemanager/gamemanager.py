from deck.deck import Deck
from player.player import User, Dealer
from player.player import PlayerStatus
from ui.frame import Frame

class GameManager:
    def __init__(self):
        self.player = None
        self.dealer = None
        self.deck = None
        self.frame = Frame()

    def __create_player(self):
        self.player = User(f"Player 1")

    def __create_dealer(self):
        self.dealer = Dealer("Dealer")

    def __create_deck(self, num_decks: int):
        deck = Deck()
        deck.create(num_decks)
        deck.shuffle()
        self.deck = deck
    
    def start_game(self, num_decks: int = 1):
        self.__create_player()
        self.__create_dealer()
        self.__create_deck(num_decks)

        self.frame.draw_frame()
        self.frame.insert_text(1, 1, "This is a test")
        self.frame.insert_text(5, 5, "This is another Test")
        self.frame.draw_frame()

        #self.__next_round()

    def display_game_status(self):
        dealer_cards = ""
        for card in self.dealer.hand:
            dealer_cards += str(card) + "\n"

        player_cards = ""
        for card in self.player.hand:
            player_cards += str(card) + "\n"
        text = f"""
====================
====================
Dealer Cards:
{dealer_cards}
Dealer Value: {self.dealer.hand_value()}
====================
Player Cards:
{player_cards}
Player Value: {self.player.hand_value()}

"""
        print(text, end='\r')


    def __next_round(self):
        # TODO: Handle empty deck
        if self.deck.deck_size < (self.deck.deck_size_init * 0.25):
            print("Need to restock the deck!")

        self.player.status = PlayerStatus.PLAYING
        self.dealer.status = PlayerStatus.PLAYING

        # First round
        self.player.play_turn(self.deck)
        self.dealer.play_turn(self.deck)
        self.display_game_status()

        # Game loop
        is_complete = False
        while not is_complete:
            is_complete = self.__next_turn()


    def __next_turn(self) -> bool:
        return True
