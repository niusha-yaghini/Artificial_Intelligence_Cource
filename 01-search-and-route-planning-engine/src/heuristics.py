import math

# This spacing is very natural for four-way grids.
def manhattan_distance(
    current,
    goal,
):
    x1, y1 = current
    x2, y2 = goal

    return abs(x1 - x2) + abs(y1 - y2)


def euclidean_distance(
    current,
    goal,
):
    x1, y1 = current
    x2, y2 = goal

    return math.sqrt(
        (x1 - x2) ** 2
        + (y1 - y2) ** 2
    )
    

# For moves where diagonal moves are also allowed with the same cost, the Chebyshev distance is useful.
def chebyshev_distance(
    current,
    goal,
):
    x1, y1 = current
    x2, y2 = goal

    return max(
        abs(x1 - x2),
        abs(y1 - y2),
    )
    

def zero_heuristic(
    current,
    goal,
):
    return 0.0
  
  
def weighted_manhattan_distance(
    current,
    goal,
):
    return 2 * manhattan_distance(
        current,
        goal,
    )
    
    
def inadmissible_weighted_manhattan(
    current,
    goal,
    minimum_step_cost=1.0,
):
    return (
        manhattan_distance(
            current,
            goal,
        )
        * minimum_step_cost
    )