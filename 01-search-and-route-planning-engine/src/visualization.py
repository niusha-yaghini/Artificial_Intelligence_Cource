# def print_grid(
#     grid,
#     start=None,
#     goal=None,
#     path=None,
# ):
#     path = set(path or [])

#     for row in range(grid.rows):
#         symbols = []

#         for col in range(grid.cols):
#             state = (row, col)

#             if state == start:
#                 symbol = "S"

#             elif state == goal:
#                 symbol = "G"

#             elif state in grid.obstacles:
#                 symbol = "#"

#             elif state in path:
#                 symbol = "*"

#             else:
#                 symbol = "."

#             symbols.append(symbol)

#         print(" ".join(symbols))


def print_grid(
    grid,
    start=None,
    goal=None,
    path=None,
    explored=None,
):
    path = set(path or [])
    explored = set(explored or [])

    for row in range(grid.rows):
        symbols = []

        for col in range(grid.cols):
            state = (row, col)

            if state == start:
                symbol = "S"

            elif state == goal:
                symbol = "G"

            elif state in grid.obstacles:
                symbol = "#"

            elif state in path:
                symbol = "*"

            elif state in explored:
                symbol = "o"

            else:
                symbol = "."

            symbols.append(symbol)

        print(" ".join(symbols))