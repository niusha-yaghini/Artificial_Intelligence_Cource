# Creating a simple Unweighted Graph.
class Graph:
    def __init__(self, directed=False):
        # directed = False => bidirectional
        self.directed = directed
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, source, destination):
        self.add_node(source)
        self.add_node(destination)

        self.adjacency_list[source].append(destination)

        if not self.directed:
            self.adjacency_list[destination].append(source)

    def neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def __contains__(self, node):
        return node in self.adjacency_list

    def __repr__(self):
        return f"Graph(directed={self.directed}, nodes={len(self.adjacency_list)})"