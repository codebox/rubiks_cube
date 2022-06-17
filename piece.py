from orientation import Orientation


class Piece:
    def __init__(self, coords):
        self.id = "{},{},{}".format(*coords)
        self.coords = coords
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

    def __eq__(self, other):
        return hasattr(other, 'coords') and hasattr(other, 'orientation') and self.coords == other.coords and self.orientation == other.orientation
