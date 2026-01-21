from gamemanager.gamemanager import GameManager

def main():
    game_manager = GameManager()
    game_manager.start_game(num_decks=4)


if __name__ == "__main__":
    main()