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
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.status = PlayerStatus.PLAYING

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
    
    def bust(self):
        raise NotImplementedError("bust not implemented")

    def win(self):
        raise NotImplementedError("win not implemented")

class Dealer(Player):
    def __init__(self, name: str):
        super().__init__(name)
        
    def play_turn(self, deck: Deck):
        if self.status == PlayerStatus.PLAYING: 
            if self.hand_value() <= 16:
                self.draw_card(deck)
                if self.hand_value() > 21:
                    self.bust()
            else:
                self.status = PlayerStatus.STAND

    def bust(self):
        self.status = PlayerStatus.BUST
            

class User(Player):
    def __init__(self, name: str):
        super().__init__(name)
        self.credits = PLAYER_START_CREDITS
        self.bet = 0

    def add_credits(self, amount: int):
        self.credits += amount

    def subtract_credits(self, amount: int):
        self.credits -= amount
        self.bet = 0
        if self.credits <= 0:
            self.status = PlayerStatus.GAMEOVER
        else:
            self.status = PlayerStatus.BUST

    def place_bet(self):
        bet = input(f"Credits: {self.credits}\nHow many credits to bet?\n")
        self.bet = int(bet)

    def play_turn(self, deck: Deck):
        # First round
        if len(self.hand) == 0:
            self.place_bet()
            self.draw_card(deck)
            self.draw_card(deck)
            if self.hand_value() > 21:
                self.bust()
            return
        # Normal round
        action = input("0) Hit\n1) Stand\n")
        action = PlayerAction(int(action))
        match action:
            case PlayerAction.STAND:
                self.status = PlayerStatus.STAND
            case PlayerAction.HIT:
                self.draw_card(deck)
                if self.hand_value() > 21:
                    self.bust()

    def bust(self):
        self.subtract_credits(self.bet)

    def win(self):
        self.add_credits(self.bet * 2)
        self.bet = 0
        

        
        