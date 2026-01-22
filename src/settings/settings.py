# Card settings
SUITS = ["club", "diamond", "heart", "spade"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Player settings
PLAYER_START_CREDITS = 1000

# UI Settings
UI_WIDTH = 100
UI_HEIGHT = 30

# Graphics
# Cards from https://www.asciiart.eu/miscellaneous/playing-cards
# Text from https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+Something+&x=none&v=4&h=4&w=80&we=false
TEXT_WIN = """
 __          ___         _ 
 \ \        / (_)       | |
  \ \  /\  / / _ _ __   | |
   \ \/  \/ / | | '_ \  | |
    \  /\  /  | | | | | |_|
     \/  \/   |_|_| |_| (_)
                           
"""
TEXT_DRAW = """
  _____                       _ 
 |  __ \                     | |
 | |  | |_ __ __ ___      __ | |
 | |  | | '__/ _` \ \ /\ / / | |
 | |__| | | | (_| |\ V  V /  |_|
 |_____/|_|  \__,_| \_/\_/   (_)
                                
"""
TEXT_GAMEOVER = """
   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                      
"""
TEXT_BUST = """
  ____            _     _ 
 |  _ \          | |   | |
 | |_) |_   _ ___| |_  | |
 |  _ <| | | / __| __| | |
 | |_) | |_| \__ \ |_  |_|
 |____/ \__,_|___/\__| (_)
                          
"""
TEXT_LOST = """
  _               _     _ 
 | |             | |   | |
 | |     ___  ___| |_  | |
 | |    / _ \/ __| __| | |
 | |___| (_) \__ \ |_  |_|
 |______\___/|___/\__| (_)
                          
"""