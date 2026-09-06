from dataclasses import dataclass
from typing import Any, Optional
from collections import deque
import heapq
from itertools import count

@dataclass
class SearchNode:
    state: Any
    parent: Optional["SearchNode"] = None
    action: Optional[Any] = None
    path_cost: float = 0.0
    depth: int = 0

@dataclass
class SearchResult:
    success: bool
    path: Optional[list[Any]]
    traversal_order: list[Any]
    nodes_expanded: int
    nodes_generated: int
    max_frontier_size: int
    solution_depth: Optional[int]
    path_cost: Optional[float]

def reconstruct_path(node: SearchNode) -> list[Any]:
    path = []
    current = node
    while current is not None:
        path.append(current.state)
        current = current.parent

    path.reverse()
    return path


# ============================================================
# BFS
# ============================================================
def bfs(environment, start, goal):
    if start not in environment:
        raise ValueError(f"Start node {start!r} does not exist in environment.")

    if goal not in environment:
        raise ValueError(f"Goal node {goal!r} does not exist in environment.")

    start_node = SearchNode(
        state=start,
        parent=None,
        depth=0,
    )

    # FIFO
    frontier = deque([start_node])
    visited = {start}
    traversal_order = []

    nodes_expanded = 0
    nodes_generated = 1
    max_frontier_size = 1

    while frontier:
        current_node = frontier.popleft()

        traversal_order.append(current_node.state)
        nodes_expanded += 1

        if current_node.state == goal:
            return SearchResult(
                success=True,
                path=reconstruct_path(current_node),
                traversal_order=traversal_order,
                nodes_expanded=nodes_expanded,
                nodes_generated=nodes_generated,
                max_frontier_size=max_frontier_size,
                solution_depth=current_node.depth,
                path_cost=current_node.path_cost,
            )

        for neighbor, edge_cost in environment.neighbors(current_node.state):
            if neighbor in visited:
                continue

            visited.add(neighbor)

            child_node = SearchNode(
                state=neighbor,
                parent=current_node,
                path_cost=(
                  current_node.path_cost
                  + edge_cost
                ),
                depth=current_node.depth + 1,
            )

            frontier.append(child_node)
            nodes_generated += 1

        max_frontier_size = max(
            max_frontier_size,
            len(frontier),
        )

    return SearchResult(
        success=False,
        path=None,
        traversal_order=traversal_order,
        nodes_expanded=nodes_expanded,
        nodes_generated=nodes_generated,
        max_frontier_size=max_frontier_size,
        solution_depth=None,
        path_cost=None,
    )
    

# ============================================================
# DFS
# ============================================================
def dfs(environment, start, goal):
    if start not in environment:
        raise ValueError(f"Start node {start!r} does not exist in environment.")

    if goal not in environment:
        raise ValueError(f"Goal node {goal!r} does not exist in environment.")

    start_node = SearchNode(
        state=start,
        parent=None,
        depth=0,
    )

    frontier = [start_node]
    visited = {start}
    traversal_order = []

    nodes_expanded = 0
    nodes_generated = 1
    max_frontier_size = 1

    while frontier:
        current_node = frontier.pop()

        traversal_order.append(current_node.state)
        nodes_expanded += 1

        if current_node.state == goal:
            return SearchResult(
                success=True,
                path=reconstruct_path(current_node),
                traversal_order=traversal_order,
                nodes_expanded=nodes_expanded,
                nodes_generated=nodes_generated,
                max_frontier_size=max_frontier_size,
                solution_depth=current_node.depth,
                path_cost=current_node.path_cost,
            )

        for neighbor, edge_cost in reversed(
            environment.neighbors(current_node.state)
        ):
            if neighbor in visited:
                continue

            visited.add(neighbor)

            child_node = SearchNode(
                state=neighbor,
                parent=current_node,
                path_cost=(
                  current_node.path_cost
                  + edge_cost
              ),
                depth=current_node.depth + 1,
            )

            frontier.append(child_node)
            nodes_generated += 1

        max_frontier_size = max(
            max_frontier_size,
            len(frontier),
        )

    return SearchResult(
        success=False,
        path=None,
        traversal_order=traversal_order,
        nodes_expanded=nodes_expanded,
        nodes_generated=nodes_generated,
        max_frontier_size=max_frontier_size,
        solution_depth=None,
        path_cost=None,
    )


# ============================================================
# DLS
# ============================================================
def depth_limited_search(
    environment,
    start,
    goal,
    depth_limit,
):
    if depth_limit < 0:
        raise ValueError("depth_limit must be non-negative.")

    if start not in environment:
        raise ValueError(
            f"Start node {start!r} does not exist in environment."
        )

    if goal not in environment:
        raise ValueError(
            f"Goal node {goal!r} does not exist in environment."
        )

    start_node = SearchNode(
        state=start,
        parent=None,
        depth=0,
    )

    frontier = [start_node]
    traversal_order = []
    nodes_expanded = 0
    nodes_generated = 1
    max_frontier_size = 1

    while frontier:
        current_node = frontier.pop()

        traversal_order.append(current_node.state)
        nodes_expanded += 1

        if current_node.state == goal:
            return SearchResult(
                success=True,
                path=reconstruct_path(current_node),
                traversal_order=traversal_order,
                nodes_expanded=nodes_expanded,
                nodes_generated=nodes_generated,
                max_frontier_size=max_frontier_size,
                solution_depth=current_node.depth,
                path_cost=current_node.path_cost,
            )

        if current_node.depth >= depth_limit:
            continue

        current_path = set(
            reconstruct_path(current_node)
        )

        for neighbor, edge_cost in reversed(
            environment.neighbors(current_node.state)
        ):
            if neighbor in current_path:
                continue

            child_node = SearchNode(
                state=neighbor,
                parent=current_node,
                path_cost=(
                  current_node.path_cost
                  + edge_cost
                ),
                depth=current_node.depth + 1,
            )

            frontier.append(child_node)
            nodes_generated += 1

        max_frontier_size = max(
            max_frontier_size,
            len(frontier),
        )

    return SearchResult(
        success=False,
        path=None,
        traversal_order=traversal_order,
        nodes_expanded=nodes_expanded,
        nodes_generated=nodes_generated,
        max_frontier_size=max_frontier_size,
        solution_depth=None,
        path_cost=None,
    )


# ============================================================
# IDDFS
# ============================================================
def iterative_deepening_dfs(
    environment,
    start,
    goal,
    max_depth,
):
    if max_depth < 0:
        raise ValueError("max_depth must be non-negative.")

    total_nodes_expanded = 0
    total_nodes_generated = 0
    overall_max_frontier_size = 0

    combined_traversal = []

    for depth_limit in range(max_depth + 1):
        result = depth_limited_search(
            environment=environment,
            start=start,
            goal=goal,
            depth_limit=depth_limit,
        )

        total_nodes_expanded += result.nodes_expanded
        total_nodes_generated += result.nodes_generated

        overall_max_frontier_size = max(
            overall_max_frontier_size,
            result.max_frontier_size,
        )

        combined_traversal.extend(
            result.traversal_order
        )

        if result.success:
            return SearchResult(
                success=True,
                path=result.path,
                traversal_order=combined_traversal,
                nodes_expanded=total_nodes_expanded,
                nodes_generated=total_nodes_generated,
                max_frontier_size=overall_max_frontier_size,
                solution_depth=result.solution_depth,
                path_cost=result.path_cost,
            )

    return SearchResult(
        success=False,
        path=None,
        traversal_order=combined_traversal,
        nodes_expanded=total_nodes_expanded,
        nodes_generated=total_nodes_generated,
        max_frontier_size=overall_max_frontier_size,
        solution_depth=None,
        path_cost=None,
    )


# ============================================================
# UCS
# ============================================================
def uniform_cost_search(
    environment,
    start,
    goal,
):
    if start not in environment:
        raise ValueError(
            f"Start node {start!r} does not exist in environment."
        )

    if goal not in environment:
        raise ValueError(
            f"Goal node {goal!r} does not exist in environment."
        )

    start_node = SearchNode(
        state=start,
        parent=None,
        path_cost=0.0,
        depth=0,
    )

    counter = count()

    frontier = []

    heapq.heappush(
        frontier,
        (
            start_node.path_cost,
            next(counter),
            start_node,
        ),
    )

    best_cost = {
        start: 0.0
    }

    traversal_order = []
    nodes_expanded = 0
    nodes_generated = 1
    max_frontier_size = 1

    while frontier:
        current_cost, _, current_node = (
            heapq.heappop(frontier)
        )

        if (
            current_cost
            > best_cost[current_node.state]
        ):
            continue

        traversal_order.append(
            current_node.state
        )

        nodes_expanded += 1

        if current_node.state == goal:
            return SearchResult(
                success=True,
                path=reconstruct_path(current_node),
                traversal_order=traversal_order,
                nodes_expanded=nodes_expanded,
                nodes_generated=nodes_generated,
                max_frontier_size=max_frontier_size,
                solution_depth=current_node.depth,
                path_cost=current_node.path_cost,
            )

        for neighbor, edge_cost in environment.neighbors(
            current_node.state
        ):
            new_cost = (
                current_node.path_cost
                + edge_cost
            )

            if (
                neighbor not in best_cost
                or new_cost < best_cost[neighbor]
            ):
                best_cost[neighbor] = new_cost

                child_node = SearchNode(
                    state=neighbor,
                    parent=current_node,
                    path_cost=new_cost,
                    depth=current_node.depth + 1,
                )

                heapq.heappush(
                    frontier,
                    (
                        new_cost,
                        next(counter),
                        child_node,
                    ),
                )

                nodes_generated += 1

        max_frontier_size = max(
            max_frontier_size,
            len(frontier),
        )

    return SearchResult(
        success=False,
        path=None,
        traversal_order=traversal_order,
        nodes_expanded=nodes_expanded,
        nodes_generated=nodes_generated,
        max_frontier_size=max_frontier_size,
        solution_depth=None,
        path_cost=None,
    )


# ============================================================
# Greedy
# ============================================================
def greedy_best_first_search(
    environment,
    start,
    goal,
    heuristic,
):
    if start not in environment:
        raise ValueError(
            f"Start node {start!r} does not exist in environment."
        )

    if goal not in environment:
        raise ValueError(
            f"Goal node {goal!r} does not exist in environment."
        )

    start_node = SearchNode(
        state=start,
        parent=None,
        path_cost=0.0,
        depth=0,
    )

    counter = count()
    frontier = []
    start_priority = heuristic(
        start,
        goal,
    )

    heapq.heappush(
        frontier,
        (
            start_priority,
            next(counter),
            start_node,
        ),
    )

    visited = {start}
    traversal_order = []
    nodes_expanded = 0
    nodes_generated = 1
    max_frontier_size = 1

    while frontier:
        _, _, current_node = heapq.heappop(
            frontier
        )

        traversal_order.append(
            current_node.state
        )

        nodes_expanded += 1

        if current_node.state == goal:
            return SearchResult(
                success=True,
                path=reconstruct_path(current_node),
                traversal_order=traversal_order,
                nodes_expanded=nodes_expanded,
                nodes_generated=nodes_generated,
                max_frontier_size=max_frontier_size,
                solution_depth=current_node.depth,
                path_cost=current_node.path_cost,
            )

        for neighbor, edge_cost in environment.neighbors(
            current_node.state
        ):
            if neighbor in visited:
                continue

            visited.add(neighbor)

            child_node = SearchNode(
                state=neighbor,
                parent=current_node,
                path_cost=(
                    current_node.path_cost
                    + edge_cost
                ),
                depth=current_node.depth + 1,
            )

            priority = heuristic(
                neighbor,
                goal,
            )

            heapq.heappush(
                frontier,
                (
                    priority,
                    next(counter),
                    child_node,
                ),
            )
            nodes_generated += 1

        max_frontier_size = max(
            max_frontier_size,
            len(frontier),
        )

    return SearchResult(
        success=False,
        path=None,
        traversal_order=traversal_order,
        nodes_expanded=nodes_expanded,
        nodes_generated=nodes_generated,
        max_frontier_size=max_frontier_size,
        solution_depth=None,
        path_cost=None,
    )
    

# ============================================================
# A*
# ============================================================
def a_star_search(
    environment,
    start,
    goal,
    heuristic,
):
    if start not in environment:
        raise ValueError(
            f"Start node {start!r} does not exist in environment."
        )

    if goal not in environment:
        raise ValueError(
            f"Goal node {goal!r} does not exist in environment."
        )

    start_node = SearchNode(
        state=start,
        parent=None,
        path_cost=0.0,
        depth=0,
    )

    counter = count()
    frontier = []
    start_priority = heuristic(
        start,
        goal,
    )

    heapq.heappush(
        frontier,
        (
            start_priority,
            next(counter),
            start_node,
        ),
    )

    best_cost = {
        start: 0.0
    }

    traversal_order = []
    nodes_expanded = 0
    nodes_generated = 1
    max_frontier_size = 1

    while frontier:
        _, _, current_node = (
            heapq.heappop(frontier)
        )

        if (
            current_node.path_cost
            > best_cost[current_node.state]
        ):
            continue

        traversal_order.append(
            current_node.state
        )

        nodes_expanded += 1

        if current_node.state == goal:
            return SearchResult(
                success=True,
                path=reconstruct_path(current_node),
                traversal_order=traversal_order,
                nodes_expanded=nodes_expanded,
                nodes_generated=nodes_generated,
                max_frontier_size=max_frontier_size,
                solution_depth=current_node.depth,
                path_cost=current_node.path_cost,
            )

        for neighbor, edge_cost in environment.neighbors(
            current_node.state
        ):
            new_cost = (
                current_node.path_cost
                + edge_cost
            )

            if (
                neighbor not in best_cost
                or new_cost < best_cost[neighbor]
            ):
                best_cost[neighbor] = new_cost

                child_node = SearchNode(
                    state=neighbor,
                    parent=current_node,
                    path_cost=new_cost,
                    depth=current_node.depth + 1,
                )

                heuristic_cost = heuristic(
                    neighbor,
                    goal,
                )

                priority = (
                    new_cost
                    + heuristic_cost
                )

                heapq.heappush(
                    frontier,
                    (
                        priority,
                        next(counter),
                        child_node,
                    ),
                )

                nodes_generated += 1

        max_frontier_size = max(
            max_frontier_size,
            len(frontier),
        )

    return SearchResult(
        success=False,
        path=None,
        traversal_order=traversal_order,
        nodes_expanded=nodes_expanded,
        nodes_generated=nodes_generated,
        max_frontier_size=max_frontier_size,
        solution_depth=None,
        path_cost=None,
    )

