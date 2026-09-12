import random


def initialize_population(
    population_size,
    chromosome_length,
):
    population = []

    for _ in range(population_size):
        chromosome = [
            random.randint(0,1)
            for _ in range(chromosome_length)
        ]
        population.append(
            chromosome
        )

    return population

def evaluate_population(
    population,
    problem,
):
    fitness_values = []

    for chromosome in population:
        fitness = problem.evaluate(
            chromosome
        )
        fitness_values.append(
            fitness
        )

    return fitness_values

def tournament_selection(
    population,
    fitness_values,
    tournament_size,
):
    tournament_indices = random.sample(
        range(len(population)),
        tournament_size,
    )
    winner_index = max(
        tournament_indices,
        key=lambda index:
        fitness_values[index],
    )
    
    return population[winner_index]

def elitism(
    population,
    fitness_values,
    elite_ratio,
):
    elite_count = int(
        len(population)
        *
        elite_ratio
    )
    ranked_indices = sorted(
        range(len(population)),
        key=lambda i: fitness_values[i],
        reverse=True,
    )
    elites = [
        population[i]
        for i in ranked_indices[:elite_count]
    ]

    return elites

def roulette_selection(
    population,
    fitness_values,
):
    total_fitness = sum(
        fitness_values
    )
    probabilities = [
        fitness / total_fitness
        for fitness in fitness_values
    ]
    selected_index = random.choices(
        range(len(population)),
        weights=probabilities,
        k=1,
    )[0]

    return population[selected_index]

def single_point_crossover(
    parent1,
    parent2,
    crossover_rate=0.8,
    crossover_point_ratio=0.5,
):
    if random.random() > crossover_rate:
        return (
            parent1.copy(),
            parent2.copy(),
        )

    point = int(
        len(parent1)
        *
        crossover_point_ratio
    )

    child1 = (
        parent1[:point]
        +
        parent2[point:]
    )

    child2 = (
        parent2[:point]
        +
        parent1[point:]
    )

    return child1, child2