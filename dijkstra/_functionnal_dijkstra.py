from typing import Optional

import numpy as np

from dijkstra.graph import Graph
from dijkstra.vertex import Vertex


def dijkstra(graph: Graph, source: Vertex, target: Optional[Vertex] = None):
    """

    :param graph:
    :param source:
    :param target: If none, compute the distance from source to each Vertex. It sets attributes 'dist' and 'prev' that
    enables finding the shortest path between source and an arbitrary target
    :return:
    """
    Q = []

    # Initialization
    for vertex in graph.vertices:
        setattr(vertex, "dist", np.inf)
        setattr(vertex, "prev", None)
        Q.append(vertex)
    setattr(source, "dist", 0)

    while len(Q) > 0:
        # Choose vertex with shortest distance 'dist'
        idx = np.argmin(getattr(v, "dist") for v in Q)
        chosen_vertex = Q.pop(idx)

        # Shortest path btw source and target
        if target is not None:
            if chosen_vertex == target:
                S = []
                vertex = target
                if (prev := getattr(vertex, "prev")) is not None or vertex == source:
                    while vertex is not None:
                        S.insert(0, vertex)
                        vertex = prev
                        prev = getattr(vertex, "prev", None)
                return S
        # Get neighbors of chosen vertex that are in Q
        neighbors = graph.get_neighbors(chosen_vertex)
        neighbors = [n for n in neighbors if n in Q]

        for n in neighbors:
            d_n = getattr(n, "dist")
            d_chosen_vertex = getattr(chosen_vertex, "dist")
            edge = graph.get_edge(chosen_vertex, n)

            if (alt := d_chosen_vertex + edge.value) < d_n:
                setattr(n, "dist", alt)
                setattr(n, "prev", chosen_vertex)
