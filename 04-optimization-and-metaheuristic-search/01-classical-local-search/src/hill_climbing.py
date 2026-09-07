def hill_climbing(
    objective_function,
    initial_state,
    get_neighbors,
):
    current = initial_state

    while True:
        neighbors = get_neighbors(
            current
        )
        current_value = objective_function(
            current
        )
        neighbor_values = [
            (
                neighbor,
                objective_function(neighbor)
            )
            for neighbor in neighbors
        ]
        best_neighbor, best_value = max(
            neighbor_values,
            key=lambda item:item[1]
        )

        if best_value <= current_value:
            break

        current = best_neighbor

    return current