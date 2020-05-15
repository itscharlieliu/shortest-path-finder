from math import sqrt

from coord import Coord


class SearchNode:
    """
    Representation of a node used in a_star
    ...
    Attributes
    ----------
    coord: coord
        The coordinates of the node on the board
    f: int
        Total cost of movement - the sum of g and h
    g: int
        Movement cost from the starting point
    h: int
        Estimated movement cost to the end point
    parent: SearchNode
        The node that this one originated from
    """

    def __init__(self, coord: Coord, g: int = 0, h: int = 0, parent=None):
        self.coord = coord
        self.f = g + h
        self.g = g
        self.h = h
        self.parent: SearchNode or None = parent
        self.is_wall = False

    def __str__(self):
        return str(int(self.is_wall))

    def __repr__(self):
        return "Coordinates: {coord} | f: {f} | g: {g} | h: {h} | Is wall: {is_wall}".format(
            coord=self.coord,
            f=round(self.f),
            g=round(self.g),
            h=round(self.h),
            is_wall=self.is_wall,
        )

    def __eq__(self, other):
        if not isinstance(other, SearchNode):
            return NotImplemented
        return self.coord == other.coord

    def __lt__(self, other):
        if not isinstance(other, SearchNode):
            return NotImplemented
        if self.f < other.f:
            return True
        return False

    def __gt__(self, other):
        if not isinstance(other, SearchNode):
            return NotImplemented
        if self.f > other.f:
            return True
        return False

    def calculate_distance(self, other):
        if not isinstance(other, SearchNode):
            return NotImplemented

        own_coords = self.coord
        other_coords = other.coord
        return sqrt(
            (((own_coords.x * 10) - (other_coords.x * 10)) ** 2)
            + (((own_coords.y * 10) - (other_coords.y * 10)) ** 2)
        )

    def print_path(self):
        if self.parent is None:
            return

        self.parent.print_path()

        print(self.__repr__(), end="\n")
