from enum import Enum

from coord import Coord
from search_node import SearchNode


class Board:
    def __init__(self, width: int = 10, height: int = 10):
        self._board = [
            [SearchNode(Coord(x, y), 0, 0) for x in range(width)] for y in range(height)
        ]

    def __str__(self):
        result = ""
        for row in self._board:
            for val in row:
                result += str(val)
            result += "\n"

        return result

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
            node = self._board[point.y][point.x]
            node.f = other.f
            node.h = other.h
            node.g = other.g
        except IndexError:
            pass
