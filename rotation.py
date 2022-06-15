class Rotation:
    def __init__(self, direction, count):
        self.direction = direction
        self.count = count % 4

    def __str__(self):
        return "{}{}".format(self.direction[0], self.count)
