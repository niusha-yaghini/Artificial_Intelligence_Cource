from math import inf
from src.metrics import SearchStats

# ============================================================
# Min-Max
# ============================================================
def minimax_decision(
    game,
    state,
):
    player = state[1]

    if player == "X":
        best_value = -inf
    else:
        best_value = inf

    best_action = None

    for action in game.actions(state):
        new_state = game.result(
            state,
            action,
        )

        value = minimax_value(
            game,
            new_state,
        )

        if player == "X":
            if value > best_value:
                best_value = value
                best_action = action
        else:
            if value < best_value:
                best_value = value
                best_action = action

    return best_action


def minimax_value(
    game,
    state,
):
    # Terminal state:
    if game.terminal_test(state):
        return game.utility(state)

    player = state[1]

    # MAX player (X)
    if player == "X":
        value = -inf

        for action in game.actions(state):
            new_state = game.result(
                state,
                action,
            )

            value = max(
                value,
                minimax_value(
                    game,
                    new_state,
                )
            )

        return value
    # MIN player (O)
    else:
        value = inf

        for action in game.actions(state):
            new_state = game.result(
                state,
                action,
            )

            value = min(
                value,
                minimax_value(
                    game,
                    new_state,
                )
            )

        return value


# ============================================================
# Min-Max + Stats
# ============================================================
def minimax_decision_with_stats(
    game,
    state,
):
    stats = SearchStats()
    player = state[1]

    if player == "X":
        best_value = -inf
    else:
        best_value = inf

    best_action = None

    for action in game.actions(state):
        value = minimax_value_with_stats(
            game,
            game.result(
                state,
                action,
            ),
            stats,
            depth=1,
        )

        if player == "X":
            if value > best_value:
                best_value = value
                best_action = action

        else:
            if value < best_value:
                best_value = value
                best_action = action

    return best_action, stats

def minimax_value_with_stats(
    game,
    state,
    stats,
    depth=0,
):
    stats.nodes_visited += 1

    stats.max_depth = max(
        stats.max_depth,
        depth,
    )

    if game.terminal_test(state):
        stats.terminals_reached += 1
        return game.utility(state)

    player = state[1]

    if player == "X":
        value = -inf

        for action in game.actions(state):
            value = max(
                value,
                minimax_value_with_stats(
                    game,
                    game.result(
                        state,
                        action,
                    ),
                    stats,
                    depth + 1,
                )
            )

        return value

    else:
        value = inf

        for action in game.actions(state):
            value = min(
                value,
                minimax_value_with_stats(
                    game,
                    game.result(
                        state,
                        action,
                    ),
                    stats,
                    depth + 1,
                )
            )

        return value
    

# ============================================================
# Depth-Limited Min-Max
# ============================================================
def depth_limited_minimax_decision(
    game,
    state,
    depth_limit,
    evaluation_function,
):
    player = state[1]

    if player == "X":
        best_value = -inf
    else:
        best_value = inf

    best_action = None

    for action in game.actions(state):
        value = depth_limited_minimax_value(
            game,
            game.result(
                state,
                action,
            ),
            depth=1,
            depth_limit=depth_limit,
            evaluation_function=evaluation_function,
        )

        if player == "X":
            if value > best_value:
                best_value = value
                best_action = action
        else:
            if value < best_value:
                best_value = value
                best_action = action

    return best_action


def depth_limited_minimax_value(
    game,
    state,
    depth,
    depth_limit,
    evaluation_function,
):
    if game.terminal_test(state):
        return game.utility(state)

    if depth == depth_limit:
        return evaluation_function(
            game,
            state,
        )

    player = state[1]

    if player == "X":
        value = -inf

        for action in game.actions(state):
            value = max(
                value,
                depth_limited_minimax_value(
                    game,
                    game.result(
                        state,
                        action,
                    ),
                    depth + 1,
                    depth_limit,
                    evaluation_function,
                )
            )
        return value

    else:
        value = inf

        for action in game.actions(state):
            value = min(
                value,
                depth_limited_minimax_value(
                    game,
                    game.result(
                        state,
                        action,
                    ),
                    depth + 1,
                    depth_limit,
                    evaluation_function,
                )
            )

        return value