from a_star import a_star
from board import Board
from coord import Coord


def main():
    board = Board()
    print(str(board))
    a_star(board, Coord(1, 1), Coord(5, 9))
    print(str(board))


if __name__ == "__main__":
    main()
