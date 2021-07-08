from dijkstra.vertex import Vertex

class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, value: float):
        self.v1 = v1
        self.v2 = v2
        self.value = value

    def has_vertex(self, vertex: Vertex) -> bool:
        return vertex in (self.v1, self.v2)

    def get_other_vertex(self, vertex: Vertex) -> Vertex:
        if vertex not in (self.v1, self.v2):
            raise ValueError("Vertex not in this edge")
        return self.v1 if vertex == self.v2 else self.v2

    def __repr__(self):
        return self.__class__.__name__ + ": (" + str(self.v1) + ", " + str(self.v2) + ", Value: " + str(self.value) + \
               ")"
