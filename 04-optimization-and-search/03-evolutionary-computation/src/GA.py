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