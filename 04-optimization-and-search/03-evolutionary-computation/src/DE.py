import numpy as np
import random


def initialize_population(
    population_size,
    dimension,
    bounds,
):
    population = []

    for _ in range(population_size):
        individual = [
            random.uniform(
                bounds[i][0],
                bounds[i][1],
            )
            for i in range(dimension)
        ]
        population.append(
            individual
        )

    return np.array(
        population
    )
    
def mutation(
    population,
    target_index,
    F=0.5,
):
    population_size = len(
        population
    )
    indices = list(
        range(population_size)
    )
    indices.remove(
        target_index
    )
    r1, r2, r3 = random.sample(
        indices,
        3,
    )

    x1 = population[r1]
    x2 = population[r2]
    x3 = population[r3]

    mutant = (
        x1
        +
        F * (x2 - x3)
    )

    return mutant

def boundary_handling(
    vector,
    bounds,
):
    vector = vector.copy()

    for i in range(
        len(vector)
    ):
        lower_bound, upper_bound = bounds[i]

        if vector[i] < lower_bound:
            vector[i] = lower_bound

        elif vector[i] > upper_bound:
            vector[i] = upper_bound

    return vector

def mutation_with_boundary(
    population,
    target_index,
    F=0.5,
    bounds=None,
):
    # Step 1:
    # Create mutant vector
    mutant = mutation(
        population,
        target_index,
        F,
    )

    # Step 2:
    # Apply boundary constraints
    if bounds is not None:
        mutant = boundary_handling(
            mutant,
            bounds,
        )

    return mutant

def crossover(
    target,
    mutant,
    CR=0.5,
):
    dimension = len(
        target
    )

    trial = target.copy()

    # Ensure at least one mutant component is selected
    j_rand = random.randint(
        0,
        dimension - 1
    )

    for j in range(
        dimension
    ):
        if (
            random.random() < CR
            or
            j == j_rand
        ):
            trial[j] = mutant[j]

    return trial