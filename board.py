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
            return self._board[point.y][point.x]
        except IndexError:
            return None

    def generate_successors(self, point: Coord):
        """
        Generate up tp 8 possible successors depending on if it is a wall
        :param point:
        :return:
        """
        successors = []

        curr = self.get_at(Coord(point.x - 1, point.y - 1))
        if curr and not curr.is_wall:
            successors.append(curr)

        curr = self.get_at(Coord(point.x, point.y - 1))
        if curr and not curr.is_wall:
            successors.append(curr)

        curr = self.get_at(Coord(point.x + 1, point.y - 1))
        if curr and not curr.is_wall:
            successors.append(curr)

        curr = self.get_at(Coord(point.x - 1, point.y))
        if curr and not curr.is_wall:
            successors.append(curr)

        curr = self.get_at(Coord(point.x + 1, point.y))
        if curr and not curr.is_wall:
            successors.append(curr)

        curr = self.get_at(Coord(point.x - 1, point.y + 1))
        if curr and not curr.is_wall:
            successors.append(curr)

        curr = self.get_at(Coord(point.x, point.y + 1))
        if curr and not curr.is_wall:
            successors.append(curr)

        curr = self.get_at(Coord(point.x + 1, point.y + 1))
        if curr and not curr.is_wall:
            successors.append(curr)

        return successors
