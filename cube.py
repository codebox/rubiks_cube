from math import trunc
from enum import Enum


class Direction(str, Enum):
    UP = 'U',
    DOWN = 'D',
    FRONT = 'F',
    BACK = 'B',
    LEFT = 'L',
    RIGHT = 'R'

class Group:
    def __init__(self, *members):
        self.members = list(members)

    def move_from(self, start_member, step_count):
        if start_member in self.members:
            return self.members[(self.members.index(start_member) + step_count) % len(self.members)]
        else:
            return start_member


right_group = Group(Direction.UP, Direction.BACK, Direction.DOWN, Direction.FRONT)
# left_group = Group(Direction.UP, Direction.FRONT, Direction.DOWN, Direction.BACK)
up_group = Group(Direction.FRONT, Direction.LEFT, Direction.BACK, Direction.RIGHT)
# down_group = Group(Direction.FRONT, Direction.RIGHT, Direction.BACK, Direction.LEFT)
front_group = Group(Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT)
# back_group = Group(Direction.UP, Direction.LEFT, Direction.DOWN, Direction.RIGHT)

class Rotation:
    '''
    A rotation of +1 along the x,y or z axis means if you are on the positive side of that axis
    looking back at the origin, there is a 90 degree clockwise rotation. So:
        U -> (0, 1, 0)
        D -> (0, -1, 0)
        R -> (1, 0, 0)
        L -> (-1, 0, 0)
        F -> (0, 0, 1)
        B -> (0, 0, -1)
    '''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def apply(self, direction):
        direction_after_x_rotation = right_group.move_from(direction, self.x)
        direction_after_x_and_y_rotation = up_group.move_from(direction_after_x_rotation, self.y)
        return front_group.move_from(direction_after_x_and_y_rotation, self.z)

    def __add__(self, other):
        return Rotation((self.x + other.x) % 4, (self.y + other.y) % 4, (self.z + other.z) % 4)

    def __str__(self):
        return "Rotation {},{},{}".format(self.x, self.y, self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


class Piece:
    def __init__(self, initial_coords):
        self.id = "{},{},{}".format(*initial_coords)
        self.initial_coords = initial_coords
        self.coords = initial_coords
        self.rotation = Rotation(0, 0, 0)

    def move(self, new_coords):
        self.coords = new_coords

    def rotate(self, rotation):
        self.rotation += rotation

    def face_value(self, face):
        return self.rotation.apply(face)

    def __str__(self):
        return "Piece[{}] {}".format(self.id, self.rotation)

    __repr__ = __str__


class Cube:
    def __init__(self, size=3):
        if size < 1:
            raise ValueError("Invalid size: {}".format(size))
        self.size = size
        self.is_odd = self.size % 2 == 1
        self.start_coord = -trunc(self.size/2)
        self.end_coord = -self.start_coord + 1
        self.pieces = self._init_pieces()

    def _init_pieces(self):
        return [
            Piece((x, y, z))
            for x in range(self.start_coord, self.end_coord) if self.is_odd or x != 0
            for y in range(self.start_coord, self.end_coord) if self.is_odd or y != 0
            for z in range(self.start_coord, self.end_coord) if self.is_odd or z != 0
        ]

    def _get_pieces_for_face(self, face):
        coord_filter = {
            Direction.UP: lambda x, y, z: y == self.end_coord - 1,
            Direction.DOWN: lambda x, y, z: y == self.start_coord,
            Direction.LEFT: lambda x, y, z: x == self.start_coord,
            Direction.RIGHT: lambda x, y, z: x == self.end_coord - 1,
            Direction.FRONT: lambda x, y, z: z == self.end_coord - 1,
            Direction.BACK: lambda x, y, z: z == self.start_coord
        }.get(face)
        return [piece for piece in self.pieces if coord_filter(*piece.coords)]

    def move(self, face, count):
        d = 1 if count > 0 else -1
        transform = {
            Direction.UP: lambda x, y, z: (-z*d, y, x*d),
            Direction.DOWN: lambda x, y, z: (z*d, y, -x*d),
            Direction.LEFT: lambda x, y, z: (x, -z*d, y*d),
            Direction.RIGHT: lambda x, y, z: (x, z*d, -y*d),
            Direction.FRONT: lambda x, y, z: (y*d, -x*d, z),
            Direction.BACK: lambda x, y, z: (-y*d, x*d, z)
        }.get(face)
        pieces_to_move = self._get_pieces_for_face(face)
        for piece in pieces_to_move:
            for _ in range(abs(count)):
                piece.move(transform(*piece.coords))
        rotation = {
            Direction.UP: Rotation(0, count, 0),
            Direction.DOWN: Rotation(0, -count, 0),
            Direction.LEFT: Rotation(-count, 0, 0),
            Direction.RIGHT: Rotation(count, 0, 0),
            Direction.FRONT: Rotation(0, 0, count),
            Direction.BACK: Rotation(0, 0, -count)
        }.get(face)
        [piece.rotate(rotation) for piece in pieces_to_move]

    def print(self):
        def face_grid(direction, get_x_coord, get_y_coord):
            grid = {}
            for piece in self._get_pieces_for_face(direction):
                grid_x = get_x_coord(piece.coords)
                grid_y = get_y_coord(piece.coords)
                piece_face_value = piece.face_value(direction)
                grid[(grid_x, grid_y)] = piece_face_value

            return grid

        def coord_transformer(i, negate=False):
            if negate:
                return lambda c: (self.size - 1) - (c[i] - self.start_coord - (1 if not self.is_odd and c[i] > 0 else 0))
            else:
                return lambda c: (c[i] - self.start_coord - (1 if not self.is_odd and c[i] > 0 else 0))

        u_grid = face_grid(Direction.UP, coord_transformer(0), coord_transformer(2))
        f_grid = face_grid(Direction.FRONT, coord_transformer(0), coord_transformer(1))
        l_grid = face_grid(Direction.LEFT, coord_transformer(2), coord_transformer(1))
        r_grid = face_grid(Direction.RIGHT, coord_transformer(2, True), coord_transformer(1))
        d_grid = face_grid(Direction.DOWN, coord_transformer(0), coord_transformer(2))
        b_grid = face_grid(Direction.BACK, coord_transformer(0), coord_transformer(1))

        full_grid = {}
        def add_to_full_grid(face_grid, x_offset, y_offset):
            for face_grid_coord, face_value in face_grid.items():
                full_grid[(face_grid_coord[0] + x_offset, face_grid_coord[1] + y_offset)] = face_value

        add_to_full_grid(u_grid, self.size, 0)
        add_to_full_grid(l_grid, 0, self.size)
        add_to_full_grid(f_grid, self.size, self.size)
        add_to_full_grid(r_grid, self.size * 2, self.size)
        add_to_full_grid(d_grid, self.size, self.size * 2)
        add_to_full_grid(b_grid, self.size, self.size * 3)

        grid_txt = ''
        for y in range(0, self.size * 4):
            for x in range(0, self.size * 3):
                c = (x,y)
                grid_txt += full_grid[c] if c in full_grid else ' '
            grid_txt += '\n'

        print(grid_txt)

    def __str__(self):
        return "{0}x{0} cube with {1} pieces {2}".format(self.size, len(self.pieces), self.pieces)
