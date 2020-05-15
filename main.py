from a_star import a_star
from board import Board
from coord import Coord


def main():
    board = Board()
    print(str(board))
    board.set_wall(Coord(5, 5))
    board.set_wall(Coord(4, 5))
    board.set_wall(Coord(3, 5))
    board.set_wall(Coord(2, 5))
    board.set_wall(Coord(1, 5))
    board.set_wall(Coord(0, 5))
    board.set_wall(Coord(6, 5))
    board.set_wall(Coord(7, 5))
    board.set_wall(Coord(8, 5))
    a_star(board, Coord(1, 1), Coord(5, 9))
    print(str(board))


if __name__ == "__main__":
    main()
