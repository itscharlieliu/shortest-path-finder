from a_star import a_star
from board import Board
from coord import Coord


def main():
    board = Board()
    board.get_at(Coord(1000, 3))
    print(str(board))
    a_star(board, Coord(0, 0), Coord(5, 9))


if __name__ == "__main__":
    main()
