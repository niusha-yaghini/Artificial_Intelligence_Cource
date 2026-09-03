import time

def measure_execution_time(
    algorithm,
    *args,
    **kwargs,
):
    start_time = time.perf_counter()

    result = algorithm(
        *args,
        **kwargs
    )

    end_time = time.perf_counter()

    elapsed_time = (
        end_time - start_time
    )

    return result, elapsed_time
  
  
def benchmark_algorithm(
    name,
    algorithm,
    *args,
    **kwargs,
):

    result, execution_time = (
        measure_execution_time(
            algorithm,
            *args,
            **kwargs,
        )
    )

    return {
        "Algorithm": name,
        "Success": result.success,
        "Path Length": result.solution_depth,
        "Path Cost": result.path_cost,
        "Nodes Expanded": result.nodes_expanded,
        "Nodes Generated": result.nodes_generated,
        "Max Frontier": result.max_frontier_size,
        "Execution Time": execution_time,
    }
    
    
def summarize_results(df):

    return (
        df
        .groupby("Algorithm")
        .agg(
            {
                "Success": "mean",
                "Path Cost": "mean",
                "Nodes Expanded": "mean",
                "Nodes Generated": "mean",
                "Execution Time": "mean",
            }
        )
        .reset_index()
    )