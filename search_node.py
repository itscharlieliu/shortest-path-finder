from enum import Enum
from math import sqrt

from EscapeCodes import EscapeCodes
from coord import Coord


class NodeType(Enum):
    none = 0
    wall = 1
    path = 2
    important = 3
    open = 4
    closed = 5


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
        self._type: NodeType = NodeType.none

    def __str__(self):
        switcher = {
            NodeType.none: "-",
            NodeType.wall: "█",
            NodeType.path: "{}▓{}".format(EscapeCodes.green, EscapeCodes.none),
            NodeType.important: "@",
            NodeType.open: "░",
            NodeType.closed: "▒",
        }

        return switcher.get(self._type, "_")

    def __repr__(self):
        return (
            "Coordinates: {coord} | f: {f} | g: {g} | h: {h} | "
            "Type: {type}".format(
                coord=self.coord,
                f=round(self.f),
                g=round(self.g),
                h=round(self.h),
                type=self._type,
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

    def set_type(self, node_type: NodeType, force=False):
        if self._type is NodeType.important:
            # Don't override important nodes
            return
        if not force and self._type == NodeType.wall:
            return
        self._type = node_type

    def get_type(self):
        return self._type

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

        self.set_type(NodeType.path)
        if self.parent is None:
            return
        self.parent.set_path()

    def copy(self):
        new_node = SearchNode(self.coord, self.g, self.h, self.parent)
        new_node.f = self.f
        new_node.set_type(self._type)

        return new_node
