from direction import Direction
from math import trunc


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

    def is_valid_for_cube_size(self, cube_size):
        is_even = cube_size % 2 == 0
        max_slice_num = max(abs(num) for num in self.slice_numbers)
        if is_even:
            return 0 not in self.slice_numbers and max_slice_num <= cube_size/2
        else:
            return max_slice_num <= trunc(cube_size/2)

    def __str__(self):
        return '{}{}{}'.format(self.direction, self.slice_numbers, self.count)