import time
from src.solvers import (
    backtracking_search_with_stats,
    backtracking_search_mrv_with_stats,
    backtracking_search_mrv_degree_with_stats,
)

def run_solver_experiment(
    problem,
    solver,
):
    start_time = time.perf_counter()

    solution, stats = solver(
        problem
    )

    end_time = time.perf_counter()

    result = stats.summary()

    result["Success"] = solution is not None
    result["Execution Time"] = (
        end_time - start_time
    )

    return result