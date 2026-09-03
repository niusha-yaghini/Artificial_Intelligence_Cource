# Search and Route Planning with Classical AI Algorithms

This project implements and evaluates classical AI search algorithms for route planning problems. The goal is to understand the behavior, trade-offs, and limitations of uninformed, informed, and cost-based search strategies.


01-search-and-route-planning/
│
├── 01_search_problem_and_graph_basics.ipynb
├── 02_bfs_and_dfs_from_scratch.ipynb
├── 03_uniform_cost_search.ipynb
├── 04_heuristic_search_greedy_and_astar.ipynb
├── 05_grid_route_planning.ipynb
├── 06_search_algorithm_benchmark.ipynb
├── src/
│   ├── config.py
│   ├── experiments.py
│   ├── search.py
│   ├── graph.py
│   ├── grid.py
│   ├── heuristics.py
│   ├── metrics.py
│   └── visualization.py
├── tests/
├── results/
└── README.md

---------------------------------------------------------

01_search_problem_and_graph_basics.ipynb
Concepts:
State
State Space
Action
Transition Model
Goal
Path Cost
Graph
Search Tree
Node
Frontier
Visited

And we analyze a few small graphs manually.

02_bfs_and_dfs_from_scratch.ipynb
Queue
Stack
BFS
DFS
DLS
IDDFS
Cycle Detection
Path Reconstruction

03_uniform_cost_search.ipynb
Weighted Graph
Priority Queue
heapq
Path Cost
UCS
Dijkstra connection

04_heuristic_search_greedy_and_astar.ipynb
Heuristic
Manhattan
Euclidean
Greedy
A*
Admissibility
Consistency

05_grid_route_planning.ipynb

Main project:
Grid
Obstacle
Weighted Terrain
Start
Goal
Search Visualization
06_search_algorithm_benchmark.ipynb


Final comparison:
BFS
DFS
UCS
Greedy
A*

In terms of:
Time
Memory
Expanded Nodes
Path Length
Path Cost
Success Rate

------------------------------

### Uninformed Search

- Breadth First Search (BFS)
- Depth First Search (DFS)

### Cost-Based Search

- Uniform Cost Search (UCS)

### Informed Search

- Greedy Best First Search
- A*


The project includes:

- Graph-based environments
- Grid-based navigation
- Obstacles
- Weighted terrain costs


Key Concepts Demonstrated:

- State representation
- Frontier management
- Explored set
- Path reconstruction
- Heuristic functions
- Optimality
- Completeness
- Time complexity
- Space complexity


