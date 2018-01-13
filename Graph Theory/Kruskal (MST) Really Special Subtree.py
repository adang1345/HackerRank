import queue


class Graph:
    def __init__(self, v, e):
        """Initialize vertices and edges. v is a set of Vertices, and e is a set of Edges."""
        for x in v:
            assert isinstance(x, Vertex)
        for x in e:
            assert isinstance(x, Edge)
        self.v = v
        self.e = e

    def __repr__(self):
        return repr(self.v) + "\n" + repr(self.e)

    def add_edge(self, edge):
        """Add edge u to the graph.
        Precondition: u is an Edge whose vertices are part of this graph"""
        assert isinstance(edge, Edge)
        self.e.add(edge)

    def neighbors(self, u):
        """Return the set of neighbors of vertex u.
        Precondition: u is part of this graph"""
        assert isinstance(u, Vertex)
        n = set()
        for edge in self.e:
            if u in edge.vertices:
                n.add(next(iter(edge.vertices.difference({u}))))
        return n

    def component(self, u):
        """Return the component of the graph that contains vertex u.
        Precondition: u is part of this graph"""
        assert isinstance(u, Vertex)
        reachable = {u}
        to_check = queue.Queue(-1)
        for n in self.neighbors(u):
            to_check.put(n)
        while not to_check.empty():
            a = to_check.get()
            if a not in reachable:
                reachable.add(a)
                for n in self.neighbors(a):
                    to_check.put(n)
        return reachable

    def total_weight(self):
        """Return the total weight of the edges"""
        return sum(edge.weight for edge in self.e)


class Vertex:
    def __init__(self, name):
        """Initialize a Vertex.
        Precondition: name is an int"""
        assert type(name) == int
        self.name = name

    def __repr__(self):
        return "Vertex" + str(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Edge:
    def __init__(self, vertices, weight):
        """Initialize an Edge.
        Precondition: vertices is a set of two Vertices, weight is an int"""
        for x in vertices:
            assert isinstance(x, Vertex)
        assert len(vertices) == 2
        assert type(weight) == int
        self.vertices = vertices
        self.weight = weight

    def __lt__(self, other):
        """Allow edges to be sorted by weight"""
        return self.weight < other.weight

    def __repr__(self):
        return "(" + repr(self.vertices) + "," + repr(self.weight) + ")"


# construct graph from distance matrix
vertices = set()
edges = set()
n = int(input().split()[1])
for _ in range(n):
    line = [int(x) for x in input().split()]
    v1 = Vertex(line[0])
    v2 = Vertex(line[1])
    vertices.add(v1)
    vertices.add(v2)
    edges.add(Edge({v1, v2}, line[2]))

graph = Graph(vertices, edges)

# perform Kruskal's algorithm
tree = Graph(vertices, set())
edges = list(edges)
edges.sort()
for edge in edges:
    edge_vertices = list(edge.vertices)
    if edge_vertices[0] not in tree.component(edge_vertices[1]):
        tree.add_edge(edge)
optimal_weight = tree.total_weight()
print(optimal_weight)
