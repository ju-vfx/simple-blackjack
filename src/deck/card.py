SPADE = " _____ \n|%s .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____%s|"
DIAMOND = " _____ \n|%s ^  |\n| / \ |\n| \ / |\n|  .  |\n|____%s|"
CLUB = " _____ \n|%s _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____%s|"
HEART = " _____ \n|%s_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____%s|"

class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        match self.suit:
            case "club":
                return f" _______ \n|{self.rank:2} _   |\n|  ( )  |\n| (_'_) |\n|   |   |\n|_____{self.rank:_>2}|"
            case "diamond":
                return f" _______ \n|{self.rank:2} ^   |\n|  / \  |\n|  \ /  |\n|   .   |\n|_____{self.rank:_>2}|"
            case "heart":
                return f" _______ \n|{self.rank:2}_ _  |\n| ( v ) |\n|  \ /  |\n|   .   |\n|_____{self.rank:_>2}|"
            case "spade":
                return f" _______ \n|{self.rank:2} .   |\n|  /.\  |\n| (_._) |\n|   |   |\n|_____{self.rank:_>2}|"

    def __repr__(self):
        return f"{self.rank} of {self.suit}"