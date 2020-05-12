from typing import List

from board import Board, Coordinates


class SearchNode:
    """
    Representation of a node used in a_star
    ...
    Attributes
    ----------
    coordinates: Coordinates
        The coordinates of the node on the board
    f: int
        Total cost of movement - the sum of g and h
    g: int
        Movement cost from the starting point
    h: int
        Estimated movement cost to the end point
    """

    def __init__(self, coordinates: Coordinates, g: int, h: int):
        self.coordinates: coordinates
        self.f = g + h
        self.g = g
        self.h = h

    def __eq__(self, other):
        if not isinstance(other, SearchNode):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.f == other.f and self.g == other.g and self.h == other.h

    def __lt__(self, other):
        if not isinstance(other, SearchNode):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.f < other.f or self.h < other.h

    def __gt__(self, other):
        if not isinstance(other, SearchNode):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.f > other.f or self.h > other.h


def a_star(board: Board, start: Coordinates, end: Coordinates):
    # TODO change this to tree for optimization
    open_list: List[SearchNode] = []
    closed_list: List[SearchNode] = [SearchNode(start, 0, 0)]
