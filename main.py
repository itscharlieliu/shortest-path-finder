from board import Board
from board import Board, Coordinates


def main():
    board = Board()
    board.set_at(Coordinates(1, 0))
    print(str(board))


if __name__ == "__main__":
    main()
