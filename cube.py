from math import trunc


class Piece:
    def __init__(self, id, orientation):
        self.id = id
        self.orientation = orientation

    def __str__(self):
        return "Piece[{}] {}".format(self.id, self.orientation)

    __repr__ = __str__


class Cube:
    def __init__(self, size=3):
        self.size = size
        self.pieces = self._init_pieces()

    def _init_pieces(self):
        is_odd = self.size % 2 == 1
        start_coord = -trunc(self.size/2)
        end_coord = -start_coord + 1
        coords = [
            (x, y, z)
            for x in range(start_coord, end_coord) if is_odd or x != 0
            for y in range(start_coord, end_coord) if is_odd or y != 0
            for z in range(start_coord, end_coord) if is_odd or z != 0
        ]
        return {c: Piece("{},{},{}".format(*c), 'u') for c in coords}

    def __str__(self):
        return "{0}x{0} cube with {1} pieces {2}".format(self.size, len(self.pieces), self.pieces)
