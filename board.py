from coord import Coord
from search_node import SearchNode, NodeType


class Board:
    def __init__(self, width: int = 10, height: int = 10):
        self._board = [
            [SearchNode(Coord(x, y), 0, 0) for x in range(width)] for y in range(height)
        ]
        self._height = height

    def __str__(self):
        result = ""
        result += "\n"
        for row in self._board:
            for val in row:
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
