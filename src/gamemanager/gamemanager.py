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

        self.frame.insert_element(80, 1, f"{'Credits':<15}\n{self.player.credits:<15}")

        if len(self.dealer.hand) > 0:
            for i, card in enumerate(self.dealer.hand):
                self.frame.insert_element(10 + ((9 * i)), 5, str(card))
            self.frame.insert_element(3, 8, f"{self.dealer.hand_value()}")

        if len(self.player.hand) > 0:
            for i, card in enumerate(self.player.hand):
                self.frame.insert_element(10 + ((9 * i)), 15, str(card))
            self.frame.insert_element(3, 18, f"{self.player.hand_value()}")

        self.frame.draw_frame()

    def __next_round(self):
        # TODO: Handle empty deck
        if self.deck.deck_size < (self.deck.deck_size_init * 0.25):
            print("Need to restock the deck!")

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


    def __status_win(self):
        self.frame.insert_element(25, 10, TEXT_WIN)
        self.frame.draw_frame()
        input()
        self.__next_round()

    def __status_draw(self):
        text = """
  _____                       _ 
 |  __ \                     | |
 | |  | |_ __ __ ___      __ | |
 | |  | | '__/ _` \ \ /\ / / | |
 | |__| | | | (_| |\ V  V /  |_|
 |_____/|_|  \__,_| \_/\_/   (_)
                                
"""
        self.frame.insert_element(25, 10, text)
        self.frame.draw_frame()
        input()
        self.__next_round()

    def __status_gameover(self):
        text = """
   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                      
"""
        self.frame.insert_element(25, 10, text)
        self.frame.draw_frame()

    def __status_bust(self):
        text = """
  ____            _     _ 
 |  _ \          | |   | |
 | |_) |_   _ ___| |_  | |
 |  _ <| | | / __| __| | |
 | |_) | |_| \__ \ |_  |_|
 |____/ \__,_|___/\__| (_)
                          
"""
        self.frame.insert_element(25, 10, text)
        self.frame.draw_frame()
        input()
        self.__next_round()

    def __status_lost(self):
        text = """
  _               _     _ 
 | |             | |   | |
 | |     ___  ___| |_  | |
 | |    / _ \/ __| __| | |
 | |___| (_) \__ \ |_  |_|
 |______\___/|___/\__| (_)
                          
"""
        self.frame.insert_element(25, 10, text)
        self.frame.draw_frame()
        input()
        self.__next_round()
    
    def __next_turn(self) -> bool:
        self.update_game_status()
        if self.player.status == PlayerStatus.PLAYING:
            self.player.play_turn(self.deck)
            if self.player.status == PlayerStatus.BUST:
                return True
            self.update_game_status()
        if self.dealer.status == PlayerStatus.PLAYING:
            self.dealer.play_turn(self.deck)
            self.update_game_status()
        
        if not self.player.status == PlayerStatus.PLAYING and not self.dealer.status == PlayerStatus.PLAYING:
            return True
        else:
            return False
