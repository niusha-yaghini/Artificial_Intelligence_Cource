# Search and Route Planning with Classical AI Algorithms

This project implements and evaluates classical AI search algorithms for route planning problems. The goal is to understand the behavior, trade-offs, and limitations of uninformed, informed, and cost-based search strategies.


01-search-and-route-planning/
│
├── 01_bfs_and_dfs_from_scratch.ipynb
├── 02_uniform_cost_search.ipynb
├── 03_heuristic_search_greedy_and_astar.ipynb
├── 04_grid_route_planning.ipynb
├── 05_search_algorithm_benchmark.ipynb
├── src/
│   ├── config.py
│   ├── experiments.py
│   ├── search.py
│   ├── graph.py
│   ├── grid.py
│   ├── heuristics.py
│   ├── metrics.py
│   └── visualization.py
├── results/
└── README.md

---------------------------------------------------------

01_bfs_and_dfs_from_scratch.ipynb
Queue
Stack
BFS
DFS
DLS
IDDFS
Cycle Detection
Path Reconstruction

02_uniform_cost_search.ipynb
Weighted Graph
Priority Queue
heapq
Path Cost
UCS
Dijkstra connection

03_heuristic_search_greedy_and_astar.ipynb
Heuristic
Manhattan
Euclidean
Greedy
A*
Admissibility
Consistency

04_grid_route_planning.ipynb
Main project:
Grid
Obstacle
Weighted Terrain
Start
Goal
Search Visualization

05_search_algorithm_benchmark.ipynb

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
