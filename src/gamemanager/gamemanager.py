from deck.deck import Deck
from player.player import User, Dealer
from player.player import PlayerStatus
from ui.frame import Frame
from settings.settings import TEXT_WIN, TEXT_LOST, TEXT_BUST, TEXT_DRAW, TEXT_GAMEOVER

class GameManager:
    def __init__(self):
        self.player = None
        self.dealer = None
        self.deck = None
        self.frame = Frame()

    def __create_player(self):
        self.player = User(f"Player 1", self)

    def __create_dealer(self):
        self.dealer = Dealer("Dealer", self)

    def __create_deck(self, num_decks: int):
        deck = Deck()
        deck.create(num_decks)
        deck.shuffle()
        self.deck = deck
    
    def start_game(self, num_decks: int = 1):
        self.__create_player()
        self.__create_dealer()
        self.__create_deck(num_decks)

        self.__next_round()

    def update_game_status(self):
        self.frame.clear_frame()
        credits_text = f"""
X-------------------------X
|         CREDITS         |
|{self.player.credits: ^25}|
X-------------------------X
"""
        self.frame.insert_element(99-29, 1, credits_text)

        if len(self.dealer.hand) > 0:
            for i, card in enumerate(self.dealer.hand):
                self.frame.insert_element(15 + ((9 * i)), 8, str(card))
            self.frame.insert_element(3, 11, f"Dealer: {self.dealer.hand_value()}")

        if len(self.player.hand) > 0:
            for i, card in enumerate(self.player.hand):
                self.frame.insert_element(15 + ((9 * i)), 15, str(card))
            self.frame.insert_element(3, 18, f"Player: {self.player.hand_value()}")

        self.frame.draw_frame()

    def __next_round(self):
        if self.deck.deck_size < (self.deck.deck_size_init * 0.25):
            self.deck.create(4)
            self.deck.shuffle()

        self.player.status = PlayerStatus.PLAYING
        self.player.bet = 0
        self.player.hand = []
        self.dealer.status = PlayerStatus.PLAYING
        self.dealer.hand = []

        # Game loop
        is_complete = False
        while not is_complete:
            is_complete = self.__next_turn()

        # Check status after game
        if self.player.status == PlayerStatus.STAND and self.dealer.status == PlayerStatus.STAND:
            if self.player.hand_value() == self.dealer.hand_value():
                self.__status_draw()
            if self.player.hand_value() > self.dealer.hand_value():
                self.player.add_credits(self.player.bet * 2)
                self.__status_win()
            if self.player.hand_value() < self.dealer.hand_value():
                self.player.subtract_credits(self.player.bet)
                if self.player.status == PlayerStatus.GAMEOVER:
                    self.__status_gameover()
                    return
                self.__status_lost()

        elif self.player.status == PlayerStatus.BUST:
            self.player.subtract_credits(self.player.bet)
            if self.player.status == PlayerStatus.GAMEOVER:
                self.__status_gameover()
                return
            self.__status_bust()

        elif self.dealer.status == PlayerStatus.BUST:
            self.player.add_credits(self.player.bet * 2)
            self.__status_win()

        else:
            raise Exception("Unknown game status")
        
    def __next_turn(self) -> bool:
        self.update_game_status()
        if self.player.status == PlayerStatus.PLAYING:
            self.player.play_turn(self.deck)
            self.update_game_status()
            if self.player.status == PlayerStatus.BUST:
                return True
        if self.dealer.status == PlayerStatus.PLAYING:
            self.dealer.play_turn(self.deck)
            self.update_game_status()
        
        self.update_game_status()

        if not self.player.status == PlayerStatus.PLAYING and not self.dealer.status == PlayerStatus.PLAYING:
            return True
        else:
            return False

    def __status_win(self):
        self.frame.insert_element(50-18, 15-5, TEXT_WIN)
        self.frame.draw_frame()
        input()
        self.__next_round()

    def __status_draw(self):
        self.frame.insert_element(50-19, 15-5, TEXT_DRAW)
        self.frame.draw_frame()
        input()
        self.__next_round()

    def __status_gameover(self):
        self.frame.insert_element(50-30, 15-5, TEXT_GAMEOVER)
        self.frame.draw_frame()

    def __status_bust(self):
        self.frame.insert_element(50-16, 15-5, TEXT_BUST)
        self.frame.draw_frame()
        input()
        self.__next_round()

    def __status_lost(self):
        self.frame.insert_element(50-16, 15-5, TEXT_LOST)
        self.frame.draw_frame()
        input()
        self.__next_round()
