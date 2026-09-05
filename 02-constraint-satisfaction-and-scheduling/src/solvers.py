from src.metrics import SolverStats


def backtracking_search(csp):
    return backtrack(
        csp,
        {}
    )

def backtrack(
    csp,
    assignment,
):
    if len(assignment) == len(
        csp.variables
    ):
        return assignment

    variable = None

    for v in csp.variables:
        if v not in assignment:
            variable = v
            break

    for value in csp.domains[variable]:
        assignment[variable] = value

        if csp.is_consistent(
            assignment
        ):
            result = backtrack(
                csp,
                assignment
            )
            if result:
                return result

        del assignment[variable]

    return None


def backtracking_search_mrv(csp):

    return backtrack_mrv(
        csp,
        {}
    )
    
def backtrack_mrv(
    csp,
    assignment,
):
    if len(assignment) == len(csp.variables):
        return assignment

    variable = select_unassigned_variable_mrv(
        csp,
        assignment,
    )

    for value in csp.domains[variable]:
        assignment[variable] = value
        if csp.is_consistent(
            assignment
        ):
            result = backtrack_mrv(
                csp,
                assignment,
            )
            if result:
                return result

        del assignment[variable]

    return None


# Static MRV
def select_unassigned_variable_mrv(
    csp,
    assignment,
):
    unassigned = [
        variable
        for variable in csp.variables
        if variable not in assignment
    ]

    return min(
        unassigned,
        key=lambda variable:
            len(csp.domains[variable])
    )
    

def backtracking_search_mrv_degree(csp):
    return backtrack_mrv_degree(
        csp,
        {}
    )
    
def backtrack_mrv_degree(
    csp,
    assignment,
):
    if len(assignment) == len(csp.variables):
        return assignment

    variable = select_unassigned_variable_mrv_degree(
        csp,
        assignment,
    )

    for value in csp.domains[variable]:
        assignment[variable] = value

        if csp.is_consistent(
            assignment
        ):
            result = backtrack_mrv_degree(
                csp,
                assignment,
            )
            if result:
                return result

        del assignment[variable]

    return None
    
def select_unassigned_variable_mrv_degree(
    csp,
    assignment,
):
    unassigned = [
        variable
        for variable in csp.variables
        if variable not in assignment
    ]
    
    return min(
        unassigned,
        key=lambda variable: (
            len(csp.domains[variable]),
            -len(csp.neighbors[variable])
        )
    )
    

# Functions with stats

def backtracking_search_with_stats(csp):
    stats = SolverStats()

    solution = backtrack_with_stats(
        csp,
        {},
        stats,
    )

    return solution, stats

def backtrack_with_stats(
    csp,
    assignment,
    stats,
):
    stats.nodes_visited += 1

    if len(assignment) == len(csp.variables):
        return assignment

    variable = None

    for v in csp.variables:
        if v not in assignment:
            variable = v
            break

    for value in csp.domains[variable]:
        stats.assignments_tried += 1

        assignment[variable] = value

        if csp.is_consistent(
            assignment
        ):
            result = backtrack_with_stats(
                csp,
                assignment,
                stats,
            )

            if result:
                return result

        del assignment[variable]

    stats.backtracks += 1

    return None


def backtracking_search_mrv_with_stats(csp):
    stats = SolverStats()
    solution = backtrack_mrv_with_stats(
        csp,
        {},
        stats,
    )
    return solution, stats

def backtrack_mrv_with_stats(
    csp,
    assignment,
    stats,
):
    stats.nodes_visited += 1

    if len(assignment) == len(csp.variables):
        return assignment

    variable = select_unassigned_variable_mrv(
        csp,
        assignment,
    )

    for value in csp.domains[variable]:
        stats.assignments_tried += 1

        assignment[variable] = value

        if csp.is_consistent(
            assignment
        ):
            result = backtrack_mrv_with_stats(
                csp,
                assignment,
                stats,
            )

            if result:
                return result

        del assignment[variable]

    stats.backtracks += 1

    return None


def backtracking_search_mrv_degree_with_stats(csp):
    stats = SolverStats()
    solution = backtrack_mrv_degree_with_stats(
        csp,
        {},
        stats,
    )
    return solution, stats

def backtrack_mrv_degree_with_stats(
    csp,
    assignment,
    stats,
):
    stats.nodes_visited += 1

    if len(assignment) == len(csp.variables):
        return assignment

    variable = select_unassigned_variable_mrv_degree(
        csp,
        assignment,
    )

    for value in csp.domains[variable]:
        stats.assignments_tried += 1
        assignment[variable] = value
        if csp.is_consistent(
            assignment
        ):
            result = backtrack_mrv_degree_with_stats(
                csp,
                assignment,
                stats,
            )

            if result:
                return result

        del assignment[variable]

    stats.backtracks += 1

    return None


