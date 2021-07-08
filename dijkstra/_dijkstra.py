from typing import Optional

import numpy as np

from dijkstra.graph import Graph
from dijkstra.vertex import Vertex


class Dijkstra:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.source = None
        self.Q = []

    @classmethod
    def clear_graph(cls, graph: Graph):
        for v in graph.vertices:
            delattr(v, "dist")
            delattr(v, "prev")

    def clear(self):
        self.clear_graph(self.graph)

    @classmethod
    def shortest_path(cls, graph: Graph, source: Vertex, target: Vertex) -> list[Vertex]:
        instance = cls(graph)
        instance.compute(source, target)
        result = instance.path_to(target)
        cls.clear_graph(graph)
        return result

    def compute(self, source: Vertex, target: Optional[Vertex] = None) -> None:
        """
        If target is none it computes all distances from source to all other vertices
        :param source:
        :param target:
        :return:
        """
        if source != self.source:
            self.set_source(source)

        while len(self.Q) > 0:
            # Choose vertex with shortest distance 'dist'
            idx = np.argmin(getattr(v, "dist") for v in self.Q)
            chosen_vertex = self.Q.pop(idx)

            # Shortest path btw source and target
            if target is not None and chosen_vertex == target:
                break  # It only computes
            # Get neighbors of chosen vertex that are in Q
            neighbors = self.graph.get_neighbors(chosen_vertex)
            neighbors = [n for n in neighbors if n in self.Q]

            for n in neighbors:
                d_n = getattr(n, "dist")
                d_chosen_vertex = getattr(chosen_vertex, "dist")
                edge = self.graph.get_edge(chosen_vertex, n)

                if (alt := d_chosen_vertex + edge.value) < d_n:
                    setattr(n, "dist", alt)
                    setattr(n, "prev", chosen_vertex)

    def set_source(self, source: Vertex) -> None:
        if source != self.source:
            self.Q = []
            for vertex in self.graph.vertices:
                setattr(vertex, "dist", np.inf)
                setattr(vertex, "prev", None)
                self.Q.append(vertex)
            setattr(source, "dist", 0)
            self.source = source

    def path_to(self, target: Vertex) -> list[Vertex]:
            S = []
            vertex = target
            if (prev := getattr(vertex, "prev")) is not None or vertex == self.source:
                while vertex is not None:
                    S.insert(0, vertex)
                    vertex = prev
                    prev = getattr(vertex, "prev", None)
                # One last test: if S[0] is not self.source then we should recompute
                if S[0] != self.source:
                    self.compute(self.source, target)
                    # Recursive call
                    S = self.path_to(target)
            return S
