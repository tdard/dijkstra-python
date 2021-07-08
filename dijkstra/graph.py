import numpy as np
from typing import Optional

from dijkstra.vertex import Vertex
from dijkstra.edge import Edge


class Graph:
    def __init__(self, edges: Optional[list[Edge]] = None, vertices: Optional[list[Vertex]] = None):
        if edges is None and vertices is None:
            self.edges = []
            self.vertices = []
        elif not (not (edges is None and (vertices is not None)) and not (
                (edges is not None) and vertices is None)):
            raise ValueError
        self.edges = edges
        self.vertices = vertices

    def get_edges(self, vertex: Vertex) -> list[Edge]:
        return [e for e in self.edges if e.has_vertex(vertex)]

    def add_vertex_and_edges(self, vertex: Vertex, edges: list[Edge]) -> None:
        self.vertices.append(vertex)
        self.edges.extend(edges)

    def has_vertex(self, vertex: Vertex) -> bool:
        return vertex in self.vertices

    def get_neighbors(self, vertex) -> list[Vertex]:
        edges = self.get_edges(vertex)
        neighbors = [e.get_other_vertex(vertex) for e in edges]
        return neighbors

    def get_edge(self, v1: Vertex, v2: Vertex) -> Edge:
        for e in self.edges:
            if e.has_vertex(v1) and e.has_vertex(v2):
                return e
        return Edge(v1, v2, np.inf)

    def get_edge_matrix(self) -> np.ndarray:
        """
        Matrix representation of the weights
        If we have N vertices the matrix has the size (N, N).
        :return:
        """
        n = len(self.vertices)
        matrix = np.ones(shape=(n, n), dtype="float")
        matrix = matrix * np.inf

        for e in self.edges:
            i, j, value = e.v1.id, e.v2.id, e.value
            matrix[i, j] = value
            matrix[j, i] = value

        for i in range(n):
            matrix[i, i] = 0

        return matrix
