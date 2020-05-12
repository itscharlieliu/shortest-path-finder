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

    def set_at(self, x: int, y: int, val: bool = True):
        self._board[y][x] = int(val)

    def get_at(self, x: int, y: int) -> bool:
        return bool(self._board[y][x])
