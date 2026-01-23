from deck.card import Card
from deck.deck import Deck
from settings.settings import PLAYER_START_CREDITS

from enum import Enum

class PlayerStatus(Enum):
    PLAYING = 0
    STAND = 1
    BUST = 2
    GAMEOVER = 3

class PlayerAction(Enum):
    HIT = 0
    STAND = 1

class Player:
    def __init__(self, name: str, gamemanager):
        self.name = name
        self.hand = []
        self.status = PlayerStatus.PLAYING
        self.gamemanager = gamemanager

    def draw_card(self, deck: Deck):
        card = deck.draw()
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def hand_value(self) -> int:
        aces = []
        sum = 0
        for card in self.hand:
            if card.rank == "A":
                aces.append(card)
            elif card.rank in ["J", "Q", "K"]:
                sum += 10
            else:
                sum += int(card.rank)
        for ace in aces:
            if (sum + 11) > 21:
                sum += 1
            else:
                sum += 11
        return sum

    def play_turn(self, deck: Deck):
        raise NotImplementedError("play_turn not implemented")
    

class Dealer(Player):
    def __init__(self, name: str, gamemanager):
        super().__init__(name, gamemanager)
        
    def play_turn(self, deck: Deck):
        if self.status == PlayerStatus.PLAYING: 
            if self.hand_value() <= 16:
                self.draw_card(deck)
                if self.hand_value() > 21:
                    self.status = PlayerStatus.BUST
            else:
                self.status = PlayerStatus.STAND
            

class User(Player):
    def __init__(self, name: str, gamemanager):
        super().__init__(name, gamemanager)
        self.credits = PLAYER_START_CREDITS
        self.bet = 0

    def add_credits(self, amount: int):
        self.credits += amount

    def subtract_credits(self, amount: int):
        self.credits -= amount
        if self.credits <= 0:
            self.status = PlayerStatus.GAMEOVER

    def place_bet(self):
        text = f"""
X-----------------------------------X
| CURRENT CREDITS: {str(self.credits): <17}|
|                                   |
| How many do you want to bet?      |
|                                   |
|                                   |
X-----------------------------------X
"""
        self.gamemanager.frame.store_frame()
        self.gamemanager.frame.insert_element(2, 22, text)
        self.gamemanager.frame.draw_frame()
        # Check valid input
        while True:
            try:
                bet = int(input())
                if bet <= self.credits and bet > 0:
                    self.bet = bet
                    break
                else:
                    raise Exception
            except:
                self.gamemanager.frame.insert_element(4, 27, "Please insert valid bet!")
                self.gamemanager.frame.draw_frame()

        self.gamemanager.frame.restore_frame()
        self.gamemanager.frame.draw_frame()

    def select_action(self) -> PlayerAction:
        text = f"""
X-----------------------------------X
| ACTIONS:                          |
|                                   |
| 1) Hit                            |
| 2) Stand                          |
|                                   |
X-----------------------------------X
"""
        self.gamemanager.frame.store_frame()
        self.gamemanager.frame.insert_element(2, 22, text)
        self.gamemanager.frame.draw_frame()
        action = None
        while True:
            try:
                action = int(input()) - 1
                if action in PlayerAction:
                    action = PlayerAction(action)
                    break
                else:
                    raise Exception
            except:
                self.gamemanager.frame.insert_element(4, 27, "Please select valid action!")
                self.gamemanager.frame.draw_frame()
        
        self.gamemanager.frame.restore_frame()
        self.gamemanager.frame.draw_frame()
        return action

    def play_turn(self, deck: Deck):
        # First round
        if len(self.hand) == 0:
            self.place_bet()
            self.draw_card(deck)
            self.draw_card(deck)
            return
        # Normal round
        action = self.select_action()
        match action:
            case PlayerAction.STAND:
                self.status = PlayerStatus.STAND
            case PlayerAction.HIT:
                self.draw_card(deck)
                if self.hand_value() > 21:
                    self.status = PlayerStatus.BUST
        