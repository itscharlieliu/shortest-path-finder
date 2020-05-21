from time import sleep

from EscapeCodes import EscapeCodes
from coord import Coord
from search_node import SearchNode, NodeType
from terminal_utils import clear_display

OPTIONS = "1) Edit wall | 2) Set start | 3) Set end | 4) Run A* | 0) Exit"


class Board:
    def __init__(self, width: int = 10, height: int = 10):
        self._board = [
            [SearchNode(Coord(x, y), 0, 0) for x in range(width)] for y in range(height)
        ]
        self._cursor: Coord or None = None
        self._height = height
        self._start: Coord or None = None
        self._end: Coord or None = None

    def __str__(self):
        result = ""
        for row in self._board:
            for val in row:
                string = str(val)
                if val.coord == self._start:
                    string = "ST"
                if val.coord == self._end:
                    string = "EN"
                if val.coord == self._cursor:
                    result += "{color}{val}{end}".format(
                        color=EscapeCodes.red, val=string, end=EscapeCodes.none
                    )
                    continue
                result += string
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
            else NodeType.none,
            force=True,
        )

    def get_start(self):
        return self._start

    def set_start(self, start: Coord):
        self._start = start
        self._board[start.y][start.x].set_type(NodeType.none)

    def get_end(self):
        return self._end

    def set_end(self, end: Coord):
        self._end = end
        self._board[end.y][end.x].set_type(NodeType.none)

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
    sleep(0.01)
    if clear:
        clear_display()

    print(OPTIONS)
    print(message, end="\n")
    print(board)
