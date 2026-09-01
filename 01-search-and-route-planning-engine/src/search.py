from dataclasses import dataclass
from typing import Any, Optional
from collections import deque

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


def reconstruct_path(node: SearchNode) -> list[Any]:
    path = []

    current = node

    while current is not None:
        path.append(current.state)
        current = current.parent

    path.reverse()

    return path


def bfs(graph, start, goal):
    if start not in graph:
        raise ValueError(f"Start node {start!r} does not exist in graph.")

    if goal not in graph:
        raise ValueError(f"Goal node {goal!r} does not exist in graph.")

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
            )

        for neighbor in graph.neighbors(current_node.state):
            if neighbor in visited:
                continue

            visited.add(neighbor)

            child_node = SearchNode(
                state=neighbor,
                parent=current_node,
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
    )
    

def dfs(graph, start, goal):
    if start not in graph:
        raise ValueError(f"Start node {start!r} does not exist in graph.")

    if goal not in graph:
        raise ValueError(f"Goal node {goal!r} does not exist in graph.")

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
            )

        for neighbor in reversed(
            graph.neighbors(current_node.state)
        ):
            if neighbor in visited:
                continue

            visited.add(neighbor)

            child_node = SearchNode(
                state=neighbor,
                parent=current_node,
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
    )
    

def depth_limited_search(
    graph,
    start,
    goal,
    depth_limit,
):
    if depth_limit < 0:
        raise ValueError("depth_limit must be non-negative.")

    if start not in graph:
        raise ValueError(
            f"Start node {start!r} does not exist in graph."
        )

    if goal not in graph:
        raise ValueError(
            f"Goal node {goal!r} does not exist in graph."
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
            )

        if current_node.depth >= depth_limit:
            continue

        current_path = set(
            reconstruct_path(current_node)
        )

        for neighbor in reversed(
            graph.neighbors(current_node.state)
        ):
            if neighbor in current_path:
                continue

            child_node = SearchNode(
                state=neighbor,
                parent=current_node,
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
    )


# IDDFS = Repeated DLS
def iterative_deepening_dfs(
    graph,
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
            graph=graph,
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
            )

    return SearchResult(
        success=False,
        path=None,
        traversal_order=combined_traversal,
        nodes_expanded=total_nodes_expanded,
        nodes_generated=total_nodes_generated,
        max_frontier_size=overall_max_frontier_size,
        solution_depth=None,
    )



