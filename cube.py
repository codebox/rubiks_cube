from math import trunc
from enum import Enum
import re


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


class Cube:
    move_parse_regex = re.compile('^(?P<face>[UDFBLR])(?P<count>[-2\']?)$')

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

    def _parse_move(self, move_text):
        match = Cube.move_parse_regex.search(move_text)
        if match:
            count_txt = match['count']
            count = {
                '2': 2,
                '-': -1,
                '\'': -1
            }.get(count_txt, 1)
            return Move([self.end_coord-1], Direction(match['face']), count)
        else:
            raise ValueError('Unable to parse move: {}'.format(move_text))

    def move(self, move_parts):
        [self._move(self._parse_move(move_part)) for move_part in move_parts.split()]

    def _move(self, move_details):
        pieces_affected = [piece for piece in self.pieces if move_details.affects_piece(piece)]
        self._move_pieces(pieces_affected, move_details.direction, move_details.count)

    def _move_pieces(self, pieces, direction, count):
        d = 1 if count > 0 else -1
        transform = {
            Direction.UP: lambda x, y, z: (-z*d, y, x*d),
            Direction.DOWN: lambda x, y, z: (z*d, y, -x*d),
            Direction.LEFT: lambda x, y, z: (x, -z*d, y*d),
            Direction.RIGHT: lambda x, y, z: (x, z*d, -y*d),
            Direction.FRONT: lambda x, y, z: (y*d, -x*d, z),
            Direction.BACK: lambda x, y, z: (-y*d, x*d, z)
        }.get(direction)

        for piece in pieces:
            for _ in range(abs(count)):
                piece.move(transform(*piece.coords))

        [piece.rotate(Rotation(direction, count)) for piece in pieces]

    def __str__(self):
        return "{0}x{0} cube with {1} pieces {2}".format(self.size, len(self.pieces), self.pieces)
