import math

# MCTSNode:
    # select()
    # expand()
    # simulate()
    # backpropagate()
    # mcts_search()
    # mcts_decision()

def uct_value(
        node,
        exploration_constant=1.4,
    ):
        if node.visits == 0:
            return float("inf")

        exploitation = (
            node.wins /
            node.visits
        )
        exploration = (
            exploration_constant
            *
            math.sqrt(
                math.log(
                    node.parent.visits
                )
                /
                node.visits
            )
        )
        return (
            exploitation
            +
            exploration
        )
        
def select(node):
    while node.fully_expanded() and node.children:
        node = max(
            node.children,
            key=uct_value
        )
    return node

class MCTSNode:
    def __init__(
        self,
        game,
        state,
        parent=None,
        action=None,
    ):
        self.game = game
        self.state = state
        self.parent = parent
        
        # It is the movement we have made from Parent to this Node.
        self.action = action
        self.children = []
        self.visits = 0
        self.wins = 0
        self.untried_actions = list(
            game.actions(state)
        )
          
    def fully_expanded(self):
        return len(
            self.untried_actions
        ) == 0
