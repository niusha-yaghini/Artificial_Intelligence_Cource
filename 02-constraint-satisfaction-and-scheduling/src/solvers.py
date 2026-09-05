from src.metrics import SolverStats
from src.constraint_propagation import ac3
from src.metrics import SolverStats

# ============================================================
# Basic Backtracking
# ============================================================
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


# ============================================================
# Static MRV
# ============================================================
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
    

# ============================================================
# MRV + Degree
# ============================================================
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
    

# ============================================================
# Instrumented Solvers
# ============================================================
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


# ============================================================
# Forward Checking
# ============================================================
def backtracking_search_forward_checking(
    csp,
):
    domains = csp.copy_domains()

    return backtrack_forward_checking(
        csp,
        {},
        domains,
    )
    
def backtrack_forward_checking(
    csp,
    assignment,
    domains,
):
    if len(assignment) == len(csp.variables):
        return assignment

    variable = select_unassigned_variable_mrv_degree(
        csp,
        assignment,
    )

    for value in domains[variable]:
        assignment[variable] = value

        new_domains = {
            var: domain.copy()
            for var, domain
            in domains.items()
        }

        new_domains[variable] = [
            value
        ]

        if forward_checking(
            csp,
            variable,
            assignment,
            new_domains,
        ):
            result = backtrack_forward_checking(
                csp,
                assignment,
                new_domains,
            )

            if result:
                return result

        del assignment[variable]

    return None

def forward_checking(
    csp,
    variable,
    assignment,
    domains,
):
    for neighbor in csp.neighbors[variable]:
        if neighbor in assignment:
            continue

        revised_domain = []

        for value in domains[neighbor]:
            assignment[neighbor] = value

            if csp.is_consistent(
                assignment
            ):
                revised_domain.append(
                    value
                )

            del assignment[neighbor]

        domains[neighbor] = revised_domain

        if len(domains[neighbor]) == 0:
            return False

    return True


# ============================================================
# Dynamic MRV + Forward Checking
# ============================================================
def select_unassigned_variable_dynamic_mrv_degree(
    csp,
    assignment,
    domains,
):
    unassigned = [
        variable
        for variable in csp.variables
        if variable not in assignment
    ]

    return min(
        unassigned,
        key=lambda variable: (
            len(domains[variable]),
            -sum(
                1
                for neighbor in csp.neighbors[variable]
                if neighbor not in assignment
            ),
        ),
    )
    
def backtracking_search_dynamic_mrv_forward_checking(
    csp,
):
    domains = csp.copy_domains()

    return backtrack_dynamic_mrv_forward_checking(
        csp,
        {},
        domains,
    )

def backtrack_dynamic_mrv_forward_checking(
    csp,
    assignment,
    domains,
):
    if len(assignment) == len(csp.variables):
        return assignment

    variable = (
        select_unassigned_variable_dynamic_mrv_degree(
            csp,
            assignment,
            domains,
        )
    )

    for value in domains[variable]:

        assignment[variable] = value

        new_domains = {
            var: domain.copy()
            for var, domain
            in domains.items()
        }

        new_domains[variable] = [value]

        if forward_checking(
            csp,
            variable,
            assignment,
            new_domains,
        ):

            result = (
                backtrack_dynamic_mrv_forward_checking(
                    csp,
                    assignment,
                    new_domains,
                )
            )

            if result:
                return result

        del assignment[variable]

    return None


# ============================================================
# Dynamic MRV + Forward Checking + Stats
# ============================================================
def backtracking_search_dynamic_fc_with_stats(
    csp,
):
    stats = SolverStats()

    domains = csp.copy_domains()

    solution = backtrack_dynamic_fc_with_stats(
        csp,
        {},
        domains,
        stats,
    )

    return solution, stats

def backtrack_dynamic_fc_with_stats(
    csp,
    assignment,
    domains,
    stats,
):
    stats.nodes_visited += 1

    if len(assignment) == len(csp.variables):
        return assignment

    variable = (
        select_unassigned_variable_dynamic_mrv_degree(
            csp,
            assignment,
            domains,
        )
    )

    for value in domains[variable]:
        stats.assignments_tried += 1

        assignment[variable] = value

        new_domains = {
            var: domain.copy()
            for var, domain
            in domains.items()
        }

        new_domains[variable] = [
            value
        ]

        if forward_checking(
            csp,
            variable,
            assignment,
            new_domains,
        ):
            result = backtrack_dynamic_fc_with_stats(
                csp,
                assignment,
                new_domains,
                stats,
            )

            if result:
                return result

        del assignment[variable]

    stats.backtracks += 1

    return None


# ============================================================
# AC-3
# ============================================================
def backtracking_search_ac3(
    csp,
):
    domains = csp.copy_domains()

    if not ac3(
        csp,
        domains,
    ):
        return None

    return backtrack_ac3(
        csp,
        {},
        domains,
    )

def backtrack_ac3(
    csp,
    assignment,
    domains,
):
    if len(assignment) == len(csp.variables):
        return assignment

    variable = (
        select_unassigned_variable_dynamic_mrv_degree(
            csp,
            assignment,
            domains,
        )
    )

    for value in domains[variable]:
        assignment[variable] = value

        new_domains = {
            var: domain.copy()
            for var, domain
            in domains.items()
        }

        new_domains[variable] = [
            value
        ]

        if forward_checking(
            csp,
            variable,
            assignment,
            new_domains,
        ):
            result = backtrack_ac3(
                csp,
                assignment,
                new_domains,
            )

            if result:
                return result

        del assignment[variable]

    return None


# ============================================================
# AC-3 + Stats
# ============================================================
def backtracking_search_ac3_with_stats(
    csp,
):
    stats = SolverStats()
    domains = csp.copy_domains()

    if not ac3(
        csp,
        domains,
    ):
        return None, stats

    solution = backtrack_ac3_with_stats(
        csp,
        {},
        domains,
        stats,
    )

    return solution, stats

def backtrack_ac3_with_stats(
    csp,
    assignment,
    domains,
    stats,
):
    stats.nodes_visited += 1

    if len(assignment) == len(csp.variables):
        return assignment

    variable = (
        select_unassigned_variable_dynamic_mrv_degree(
            csp,
            assignment,
            domains,
        )
    )

    for value in domains[variable]:
        stats.assignments_tried += 1

        assignment[variable] = value

        new_domains = {
            var: domain.copy()
            for var, domain
            in domains.items()
        }

        new_domains[variable] = [
            value
        ]

        if forward_checking(
            csp,
            variable,
            assignment,
            new_domains,
        ):
            result = backtrack_ac3_with_stats(
                csp,
                assignment,
                new_domains,
                stats,
            )

            if result:
                return result

        del assignment[variable]

    stats.backtracks += 1

    return None


# ============================================================
# LCV
# ============================================================
def order_values_lcv(
    csp,
    variable,
    assignment,
    domains,
):
    value_scores = []

    for value in domains[variable]:
        eliminated = 0

        assignment[variable] = value

        for neighbor in csp.neighbors[variable]:
            if neighbor in assignment:
                continue

            for neighbor_value in domains[neighbor]:
                test_assignment = {
                    variable: value,
                    neighbor: neighbor_value,
                }

                if not csp.is_consistent(
                    test_assignment
                ):
                    eliminated += 1

        del assignment[variable]

        value_scores.append(
            (
                value,
                eliminated,
            )
        )

    value_scores.sort(
        key=lambda x: x[1]
    )

    return [
        value
        for value, score
        in value_scores
    ]
    
def backtracking_search_lcv(
    csp,
):
    domains = csp.copy_domains()
    return backtrack_lcv(
        csp,
        {},
        domains,
    )
    
def backtrack_lcv(
    csp,
    assignment,
    domains,
):
    if len(assignment) == len(csp.variables):
        return assignment

    variable = (
        select_unassigned_variable_dynamic_mrv_degree(
            csp,
            assignment,
            domains,
        )
    )

    values = order_values_lcv(
        csp,
        variable,
        assignment,
        domains,
    )

    for value in values:
        assignment[variable] = value

        new_domains = {
            var: domain.copy()
            for var, domain
            in domains.items()
        }

        new_domains[variable] = [
            value
        ]

        if forward_checking(
            csp,
            variable,
            assignment,
            new_domains,
        ):
            result = backtrack_lcv(
                csp,
                assignment,
                new_domains,
            )

            if result:
                return result

        del assignment[variable]

    return None


# ============================================================
# LCV + Stats
# ============================================================
def backtracking_search_lcv_with_stats(
    csp,
):
    stats = SolverStats()
    domains = csp.copy_domains()

    solution = backtrack_lcv_with_stats(
        csp,
        {},
        domains,
        stats,
    )

    return solution, stats

def backtrack_lcv_with_stats(
    csp,
    assignment,
    domains,
    stats,
):
    stats.nodes_visited += 1

    if len(assignment) == len(csp.variables):
        return assignment

    variable = (
        select_unassigned_variable_dynamic_mrv_degree(
            csp,
            assignment,
            domains,
        )
    )

    values = order_values_lcv(
        csp,
        variable,
        assignment,
        domains,
    )

    for value in values:
        stats.assignments_tried += 1

        assignment[variable] = value

        new_domains = {
            var: domain.copy()
            for var, domain
            in domains.items()
        }

        new_domains[variable] = [
            value
        ]

        if forward_checking(
            csp,
            variable,
            assignment,
            new_domains,
        ):
            result = backtrack_lcv_with_stats(
                csp,
                assignment,
                new_domains,
                stats,
            )

            if result:
                return result

        del assignment[variable]

    stats.backtracks += 1

    return None
