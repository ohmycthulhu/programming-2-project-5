from game import Game


def main():
    # Initialize the game
    game = Game()

    # Run iterations of game until the game ends
    while game.can_continue():
        game.iterate()

    # Display winner name or message about draw
    if game.has_winner():
        game.print()
        print(f"{game.get_winner_name()} won!")
    else:
        print("Game is draw!")


if __name__ == '__main__':
    main()
