from game import Game


def main():
    # Initialize the game
    game = Game(width=7, height=7)

    # Run iterations of game until the game ends
    while game.can_continue():
        game.iterate()

    # Display winner name or message about draw
    if game.has_winner():
        game.print()
        print(f"{game.winner_name} won!")
    else:
        print("Game is draw!")


if __name__ == '__main__':
    main()
