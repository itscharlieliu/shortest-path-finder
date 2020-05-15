class Coord:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __repr__(self):
        return "( {x}, {y} )".format(x=self.x, y=self.y)

    def __eq__(self, other):
        if not isinstance(other, Coord):
            return NotImplemented
        return self.x == other.x and self.y == other.y
