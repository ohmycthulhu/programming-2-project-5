# Connect 4
This is the source code of the Project 5 pt. 2 (Connect4 with AI).
The game is in terminal mode.

## Table of content

- [How to run](#how-to-run)
- [The project's structure](#the-projects-structure)
- [The Board](#the-board)
- [AI algorithm](#ai-algorithm)

## How to run
The program requires Python 3 and _numpy_ package. To run, simply use:
`$ python3 main.py`

## The Project's structure
The main script is `main.py`. The game is consisted of 6 classes:
- _Game_ - responsible for whole game process, controls the turns, finds winners,
manages the board, and gets the move information for players.
- _Board_ - stores and manages the board (i.e. numpy array), provides methods for adding the elements.
- _Connect4_ - static class for common operations over the board in Connect4.
- _Player_ - data class that holds information about a player, i.e. name, used character. Provides methods for highlighting the
player's position on the board.
- _AI_ - provides the interface for working with the AI and generating new moves based on the board allocation.
- _AIMove_ - implements *negamax* search with *α-β* pruning, early evaluation function, and depth control.

## The Board
The board is presented by 2D numpy array with characters as values. Empty cells are presented by ' ' character,
and players by their characters. Most of the operations require numpy boolean arrays (so it's easy to be abstract,
and not depend on the player information), thus `Player` class is able to turn the game board into such array.

## AI algorithm
The algorithm is a combination of several ideas on the base of the minmax algorithm.
The main idea is using _negamax_ to simplify implementation, include *α-β pruning* to reduce the amount of explored
branches, and at the same time implement early evaluation to prevent exploring the whole branch before evaluation.
The default depth limit is _4_, but it can be changed in `AIMove.DEPTH_THRESHOLD`.

