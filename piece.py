from orientation import Orientation


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
