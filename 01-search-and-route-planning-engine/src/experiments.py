from src.grid import GridEnvironment
from src.metrics import benchmark_algorithm

def get_search_algorithms(
  bfs,
  uniform_cost_search,
  greedy_best_first_search,
  a_star_search,
  heuristic,
):
  return [
    (
      "BFS",
      bfs,
      {}
    ),
    (
      "UCS",
      uniform_cost_search,
      {}
    ),
    (
      "Greedy",
      greedy_best_first_search,
      {
        "heuristic": heuristic
      }
    ),
    (
      "A*",
      a_star_search,
      {
        "heuristic": heuristic
      }
    ),
  ]
    
    
def run_single_experiment(
  environment,
  start,
  goal,
  algorithms,
):
  results = []

  for name, algorithm, kwargs in algorithms:
    result = benchmark_algorithm(
      name,
      algorithm,
      environment,
      start,
      goal,
      **kwargs,
    )
    results.append(result)

  return results

  
def generate_solvable_grid(
  rows,
  cols,
  obstacle_probability,
  start,
  goal,
  solvability_checker,
):

  while True:
    grid = GridEnvironment.random_grid(
      rows,
      cols,
      obstacle_probability,
      start,
      goal,
    )
    result = solvability_checker(
      grid,
      start,
      goal,
    )
    if result.success:
      return grid
    
    
def generate_solvable_grid_from_config(
  config,
  solvability_checker,
):
  while True:
    grid = GridEnvironment.random_grid(
      config.rows,
      config.cols,
      config.obstacle_probability,
      config.start,
      config.goal,
    )
    result = solvability_checker(
      grid,
      config.start,
      config.goal,
    )
    if result.success:
      return grid
    
    
def run_configured_experiment(
  config,
  algorithms,
  solvability_checker,
):

  all_results = []

  for trial in range(config.trials):
    grid = generate_solvable_grid_from_config(
      config,
      solvability_checker,
    )
    results = run_single_experiment(
      grid,
      config.start,
      config.goal,
      algorithms,
    )

    for result in results:
      result["Trial"] = trial
      result["Grid Size"] = (
        f"{config.rows}x{config.cols}"
      )
      result["Obstacle Probability"] = (
        config.obstacle_probability
      )
      all_results.append(result)

  return all_results