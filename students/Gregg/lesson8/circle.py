


class Circle():
    """A circle object that has all the attributes and methods of a circle"""


    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __repr__(self):
        return f'Circle({self.radius})'
