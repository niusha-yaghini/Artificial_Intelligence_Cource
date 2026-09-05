# A new node in the Search Tree
class SolverStats:
    def __init__(self):
        self.nodes_visited = 0
        self.assignments_tried = 0
        self.backtracks = 0

    def reset(self):
        self.nodes_visited = 0
        self.assignments_tried = 0
        self.backtracks = 0

    def summary(self):
        return {
            "Nodes Visited": self.nodes_visited,
            "Assignments Tried": self.assignments_tried,
            "Backtracks": self.backtracks,
        }