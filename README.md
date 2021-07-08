This is an implementation of Dijkstra's algorithm to find the shortest path between two vertices in a (acyclic) graph

# Installation
`pip install -r requirements.txt`

`pip install .`


# Examples
```
from dijkstra import Vertex, Edge, Graph, Dijkstra, dijkstra

vertices = [Vertex(i) for i in range(3)]
edges = [Edge(vertices[0], vertices[1], 2),
         Edge(vertices[0], vertices[2], 4),
         Edge(vertices[1], vertices[2], 1)]
graph = Graph(edges, vertices)

# Print graph edges (weights) as a matrix
print(graph.get_edge_matrix())

source = vertices[0]
target = vertices[2]

# Find the shortest path in 'one-shot' way
shortest_path = Dijkstra.shortest_path(graph, source, target)
# or 
# shortest_path = dijkstra(graph, source, target)
print("Shortest path: ", shortest_path)

# Find the shortest path from source to any target
d = Dijkstra(graph)
d.compute(source)

# Compute only the 'reconstruction' of the path, not its exploration 
# (it is significantly shorter)
path_to_target_1 = d.path_to(vertices[1])
path_to_target_2 = d.path_to(vertices[2])

# Once you have no longer the use you can clear the attributes that Dijkstra 
# used on the graph
d.clear()
```

