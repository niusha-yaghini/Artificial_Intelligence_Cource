class SearchStats:
    def __init__(self):
        self.nodes_visited = 0
        self.terminals_reached = 0
        self.max_depth = 0

    def summary(self):
        return {
            "Nodes Visited": self.nodes_visited,
            "Terminal States": self.terminals_reached,
            "Max Depth": self.max_depth,
        }