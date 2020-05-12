from a_star import a_star
from board import Board, Coordinates


def main():
    board = Board()
    board.set_at(Coordinates(1, 0))
    print(str(board))
    a_star(board, Coordinates(1, 1), Coordinates(5, 9))


if __name__ == "__main__":
    main()
