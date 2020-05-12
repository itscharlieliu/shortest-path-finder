class Coordinates:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


class Board:
    def __init__(self, width: int = 10, height: int = 10):
        self._board = [[0 for x in range(width)] for y in range(height)]

    def __str__(self):
        result = ""
        for row in self._board:
            for val in row:
                result += str(val)
            result += "\n"

        return result

    def set_at(self, point: Coordinates, val: bool = True):
        self._board[point.y][point.x] = int(val)

    def get_at(self, point: Coordinates) -> bool:
        return bool(self._board[point.y][point.x])
