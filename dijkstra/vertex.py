class Vertex:
    def __init__(self, _id: int):
        self.id = _id

    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            return other.id == self.id
        return False

    def __repr__(self):
        return self.__class__.__name__ + ": " + str(self.id)
