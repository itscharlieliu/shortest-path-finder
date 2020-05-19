from EscapeCodes import EscapeCodes
from coord import Coord
from search_node import SearchNode, NodeType
from terminal_utils import clear_board


class Board:
    def __init__(self, width: int = 10, height: int = 10):
        self._board = [
            [SearchNode(Coord(x, y), 0, 0) for x in range(width)] for y in range(height)
        ]
        self._cursor: Coord or None = None
        self._height = height

    def __str__(self):
        result = ""
        for row in self._board:
            for val in row:
                if val.coord == self._cursor:
                    result += "{color}{val}{end}".format(
                        color=EscapeCodes.red, val=str(val), end=EscapeCodes.none
                    )
                    continue
                result += str(val)
            result += "\n"

        return result

    def get_height(self):
        return self._height

    def get_at(self, point: Coord) -> SearchNode or None:
        try:
            if point.x < 0 or point.y < 0:
                raise IndexError
            return self._board[point.y][point.x]
        except IndexError:
            return None

    def set_at(self, other: SearchNode):
        point = other.coord
        try:
            if point.x < 0 or point.y < 0:
                raise IndexError
            self._board[point.y][point.x] = other
        except IndexError:
            pass

    def set_wall(self, point: Coord, is_set=True):
        self._board[point.y][point.x].set_type(
            NodeType.wall if is_set else NodeType.none
        )

    def toggle_wall(self, point: Coord):
        self._board[point.y][point.x].set_type(
            NodeType.wall
            if not self._board[point.y][point.x].get_type() == NodeType.wall
            else NodeType.none
        )

    def set_cursor(self, point: Coord):
        self._cursor = point

    def get_cursor(self):
        return self._cursor

    def clear_cursor(self):
        self._cursor = None

    def clear(self):
        self._cursor = None
        for row in self._board:
            for val in row:
                val.set_type(NodeType.none)


def print_board(board, clear=True, message=""):
    if clear:
        clear_board(board.get_height() + 2)

    print(message, end="\n\n")
    print(board)
