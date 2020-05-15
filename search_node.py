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
        self.is_path = False
        self.is_important = False

    def __str__(self):
        if self.is_important:
            return "A"
        if self.is_wall:
            return "X"
        if self.is_path:
            return "O"
        return "_"

    def __repr__(self):
        return (
            "Coordinates: {coord} | f: {f} | g: {g} | h: {h} | "
            "Is wall: {is_wall} | Is path: {is_path} | Is important: {is_important}".format(
                coord=self.coord,
                f=round(self.f),
                g=round(self.g),
                h=round(self.h),
                is_wall=self.is_wall,
                is_path=self.is_path,
                is_important=self.is_important,
            )
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

    def set_path(self):
        if self.parent is None:
            return

        self.parent.set_path()

        self.is_path = True

    def copy(self):
        new_node = SearchNode(self.coord, self.g, self.h, self.parent)
        new_node.f = self.f
        new_node.is_wall = self.is_wall
        new_node.is_path = self.is_path
        new_node.is_important = self.is_important

        return new_node
