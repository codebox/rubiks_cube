from math import trunc
from enum import Enum


class Direction(str, Enum):
    UP = 'U',
    DOWN = 'D',
    FRONT = 'F',
    BACK = 'B',
    LEFT = 'L',
    RIGHT = 'R'


class Face(str, Enum):
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


class Rotation:
    def __init__(self, direction, count):
        self.direction = direction
        self.count = count % 4

    def __str__(self):
        return "{}{}".format(self.direction[0], self.count)


class Orientation:
    def __init__(self):
        self.direction_faces = {
            Direction.FRONT: Face.FRONT,
            Direction.BACK: Face.BACK,
            Direction.RIGHT: Face.RIGHT,
            Direction.LEFT: Face.LEFT,
            Direction.UP: Face.UP,
            Direction.DOWN: Face.DOWN
        }

    rotation_groups = {
        Direction.RIGHT: Group(Direction.FRONT, Direction.UP, Direction.BACK, Direction.DOWN),
        Direction.LEFT: Group(Direction.BACK, Direction.UP, Direction.FRONT, Direction.DOWN),
        Direction.UP: Group(Direction.RIGHT, Direction.FRONT, Direction.LEFT, Direction.BACK),
        Direction.DOWN: Group(Direction.LEFT, Direction.FRONT, Direction.RIGHT, Direction.BACK),
        Direction.FRONT: Group(Direction.LEFT, Direction.UP, Direction.RIGHT, Direction.DOWN),
        Direction.BACK: Group(Direction.RIGHT, Direction.UP, Direction.LEFT, Direction.DOWN)
    }

    def change(self, rotation):
        rotation_group = Orientation.rotation_groups[rotation.direction]
        self.direction_faces = {rotation_group.move_from(direction, rotation.count): face
                                for direction, face in self.direction_faces.items()}

    def get_face_for_direction(self, direction):
        return self.direction_faces[direction]


class Piece:
    def __init__(self, initial_coords):
        self.id = "{},{},{}".format(*initial_coords)
        self.initial_coords = initial_coords
        self.coords = initial_coords
        self.orientation = Orientation()

    def move(self, new_coords):
        self.coords = new_coords

    def rotate(self, rotation):
        self.orientation.change(rotation)

    def face_value(self, direction):
        return self.orientation.get_face_for_direction(direction)

    def __str__(self):
        return "Piece[{}] {}".format(self.id, self.orientation)

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

    def move(self, direction, count):
        d = 1 if count > 0 else -1
        transform = {
            Direction.UP: lambda x, y, z: (-z*d, y, x*d),
            Direction.DOWN: lambda x, y, z: (z*d, y, -x*d),
            Direction.LEFT: lambda x, y, z: (x, -z*d, y*d),
            Direction.RIGHT: lambda x, y, z: (x, z*d, -y*d),
            Direction.FRONT: lambda x, y, z: (y*d, -x*d, z),
            Direction.BACK: lambda x, y, z: (-y*d, x*d, z)
        }.get(direction)
        pieces_to_move = self._get_pieces_for_face(direction)
        for piece in pieces_to_move:
            for _ in range(abs(count)):
                piece.move(transform(*piece.coords))

        [piece.rotate(Rotation(direction, count)) for piece in pieces_to_move]

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
        f_grid = face_grid(Direction.FRONT, coord_transformer(0), coord_transformer(1, True))
        l_grid = face_grid(Direction.LEFT, coord_transformer(2), coord_transformer(1, True))
        r_grid = face_grid(Direction.RIGHT, coord_transformer(2, True), coord_transformer(1, True))
        d_grid = face_grid(Direction.DOWN, coord_transformer(0), coord_transformer(2, True))
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
        # see https://stackoverflow.com/questions/38522909/how-to-print-color-box-on-the-console-in-python
        TEMPLATE = '\033[48;5;{}m'
        COLOUR_RED = TEMPLATE.format(160)
        COLOUR_YELLOW = TEMPLATE.format(226)
        COLOUR_ORANGE = TEMPLATE.format(202)
        COLOUR_WHITE = TEMPLATE.format(15)
        COLOUR_BLUE = TEMPLATE.format(12)
        COLOUR_GREEN = TEMPLATE.format(10)
        RESET_COLOUR = '\033[0;0m'
        colour_lookup = {
            Direction.UP: COLOUR_BLUE,
            Direction.DOWN: COLOUR_GREEN,
            Direction.RIGHT: COLOUR_RED,
            Direction.LEFT: COLOUR_ORANGE,
            Direction.FRONT: COLOUR_WHITE,
            Direction.BACK: COLOUR_YELLOW,
        }
        space = '  '
        for y in range(0, self.size * 4):
            for x in range(0, self.size * 3):
                c = (x,y)
                if c in full_grid:
                    face_value = full_grid[c]
                    face_colour = colour_lookup[face_value] + space + RESET_COLOUR + ' '
                    grid_txt += face_colour
                else:
                    grid_txt += RESET_COLOUR + space + ' '
            grid_txt += '\n'

        print(grid_txt)
        print(RESET_COLOUR)

    def __str__(self):
        return "{0}x{0} cube with {1} pieces {2}".format(self.size, len(self.pieces), self.pieces)
