In Section 01 we had:
    An Agent in an environment tries to achieve a Goal.

For example: Start → Goal
And we assumed that the environment does not decide against us.

But in Game AI:
    There is another Agent whose goal is exactly the opposite of ours. That is, the environment is intelligent and competitive.

So the Tree is no longer: a simple Search Tree.
It is: a Game Tree.

-----------------------------------

We usually define a game with these 5 components:

G = (S,A,T,U,P)
State, Actions, Transition Model, Terminal Test, Utility Function (Final value of State.)

-----------------------------------

Adversarial Search comes before RL because it is more of a planning/search method, while RL is a learning method.

              Decision Making
                    |
        -------------------------
        |                       |
 Search-based Planning        Learning-based
        |                       |
 Adversarial Search            RL
        |
 Minimax
 Alpha-Beta


comparing RL and Adversarial Search:


|                         | Adversarial Search                  | RL                       |
| ----------------------- | ----------------------------------- | ------------------------ |
| Problem Type            | Decision-making against an opponent | Decision Learning        |
| Environmental Knowledge | Usually Complete                    | Usually Incomplete       |
| Learning                | No                                  | Yes                      |
| Experience Required     | No                                  | Yes                      |
| Goal                    | Current Best Move                   | Long-Term Optimal Policy |
| Algorithms              | Minimax, Alpha-Beta                 | Q-Learning, DQN, PPO     |

--------------------------------------------------------

Classic Algorithms:

Minimax
Alpha-Beta Pruning
Monte Carlo Tree Search (MCTS)

For example, AlphaZero is a combination of both:
    Neural Network from RL
    Tree Search from MCTS


examples explanations:

Minimax says: Check all paths.

Alpha-Beta says: If you are sure that a path will never be chosen, don't check it again.

MCTS says: Instead of examining the entire future, I simulate the future a few thousand times and learn from experience which moves are better.
MCTS Uses UCT (Upper Confidence Bound applied to Trees). MCTS gets better over time. in Minimax, If Depth is constant It gives the same answer. But in MCTS, The more Simulation the better the estimate.