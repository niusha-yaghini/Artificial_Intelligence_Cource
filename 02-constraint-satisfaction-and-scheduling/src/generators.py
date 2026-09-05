# The Generator's job is only to create the problem.
import random

from src.csp import CSP
from src.constraints import BinaryConstraint


def generate_variables(
    num_variables,
):
    return [
        f"X{i}"
        for i in range(num_variables)
    ]
    
def generate_domains(
    variables,
    num_colors,
):
    return {
        variable: list(range(num_colors))
        for variable in variables
    }
    
# For each pair of Variables Create a Constraint with a given probability.
def generate_constraints(
    variables,
    edge_probability,
):
    constraints = []

    neighbors = {
        variable:[]
        for variable in variables
    }

    for i in range(len(variables)):
        for j in range(i+1,len(variables)):
            if random.random() < edge_probability:
                var1 = variables[i]
                var2 = variables[j]

                constraints.append(
                    BinaryConstraint(
                        var1,
                        var2,
                    )
                )

                neighbors[var1].append(
                    var2
                )
                neighbors[var2].append(
                    var1
                )

    return constraints, neighbors


def generate_graph_coloring_csp(
    num_variables=20,
    num_colors=4,
    edge_probability=0.2,
):
    variables = generate_variables(
        num_variables
    )

    domains = generate_domains(
        variables,
        num_colors,
    )

    constraints, neighbors = generate_constraints(
        variables,
        edge_probability,
    )

    return CSP(
        variables,
        domains,
        constraints,
        neighbors,
    )