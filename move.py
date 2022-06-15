from direction import Direction


class Move:
    def __init__(self, slice_numbers, direction, count):
        self.slice_numbers = slice_numbers
        self.direction = direction
        self.count = count
        self._affects_coords = {
            Direction.UP: lambda x, y, z: y in slice_numbers,
            Direction.DOWN: lambda x, y, z: -y in slice_numbers,
            Direction.LEFT: lambda x, y, z: -x in slice_numbers,
            Direction.RIGHT: lambda x, y, z: x in slice_numbers,
            Direction.FRONT: lambda x, y, z: z in slice_numbers,
            Direction.BACK: lambda x, y, z: -z in slice_numbers
        }.get(direction)

    def affects_piece(self, piece):
        return self._affects_coords(*piece.coords)