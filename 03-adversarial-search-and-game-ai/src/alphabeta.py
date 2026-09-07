from math import inf
from src.ordering import ordered_actions

# ============================================================
# Alpha Beta
# ============================================================
def alpha_beta_value(
    game,
    state,
    alpha,
    beta,
):
    if game.terminal_test(state):
        return game.utility(state)

    player = state[1]

    # MAX player
    if player == "X":
        value = -inf

        for action in game.actions(state):
            value = max(
                value,
                alpha_beta_value(
                    game,
                    game.result(
                        state,
                        action,
                    ),
                    alpha,
                    beta,
                )
            )
            alpha = max(
                alpha,
                value,
            )
            if beta <= alpha:
                break

        return value

    # MIN player
    else:
        value = inf

        for action in game.actions(state):
            value = min(
                value,
                alpha_beta_value(
                    game,
                    game.result(
                        state,
                        action,
                    ),
                    alpha,
                    beta,
                )
            )
            beta = min(
                beta,
                value,
            )
            if beta <= alpha:
                break

        return value
    
    
def alpha_beta_decision(
    game,
    state,
):
    player = state[1]

    if player == "X":
        best_value = -inf
    else:
        best_value = inf

    best_action = None
    alpha = -inf
    beta = inf

    for action in game.actions(state):
        value = alpha_beta_value(
            game,
            game.result(
                state,
                action,
            ),
            alpha,
            beta,
        )

        if player == "X":
            if value > best_value:
                best_value = value
                best_action = action
            alpha = max(
                alpha,
                best_value,
            )
        else:
            if value < best_value:
                best_value = value
                best_action = action
            beta = min(
                beta,
                best_value,
            )

    return best_action


# ============================================================
# Alpha Beta + Stats
# ============================================================
def alpha_beta_value_with_stats(
    game,
    state,
    alpha,
    beta,
    stats,
):
    stats.nodes_visited += 1

    if game.terminal_test(state):
        stats.terminal_states += 1
        return game.utility(state)

    player = state[1]

    if player == "X":
        value = -inf
        for action in game.actions(state):
            value = max(
                value,
                alpha_beta_value_with_stats(
                    game,
                    game.result(
                        state,
                        action,
                    ),
                    alpha,
                    beta,
                    stats,
                )
            )
            alpha = max(
                alpha,
                value,
            )
            if beta <= alpha:
                break
        return value
    else:
        value = inf
        for action in game.actions(state):
            value = min(
                value,
                alpha_beta_value_with_stats(
                    game,
                    game.result(
                        state,
                        action,
                    ),
                    alpha,
                    beta,
                    stats,
                )
            )
            beta = min(
                beta,
                value,
            )
            if beta <= alpha:
                break

        return value
    
    
# ============================================================
# Alpha Beta + Ordering Heuristic
# ============================================================
def alpha_beta_value_ordered(
    game,
    state,
    alpha,
    beta,
):
    if game.terminal_test(state):
        return game.utility(state)

    player = state[1]

    if player == "X":
        value = -inf

        for action in ordered_actions(
            game,
            state,
        ):
            value = max(
                value,
                alpha_beta_value_ordered(
                    game,
                    game.result(
                        state,
                        action,
                    ),
                    alpha,
                    beta,
                )
            )
            alpha = max(
                alpha,
                value,
            )
            if beta <= alpha:
                break
        return value
    else:
        value = inf
        for action in ordered_actions(
            game,
            state,
        ):
            value = min(
                value,
                alpha_beta_value_ordered(
                    game,
                    game.result(
                        state,
                        action,
                    ),
                    alpha,
                    beta,
                )
            )
            beta = min(
                beta,
                value,
            )
            if beta <= alpha:
                break

        return value
    
def alpha_beta_decision_ordered(
    game,
    state,
):
    player = state[1]

    if player == "X":
        best_value = -inf
    else:
        best_value = inf

    best_action = None
    alpha = -inf
    beta = inf

    for action in ordered_actions(
        game,
        state,
    ):
        value = alpha_beta_value_ordered(
            game,
            game.result(
                state,
                action,
            ),
            alpha,
            beta,
        )

        if player == "X":
            if value > best_value:
                best_value = value
                best_action = action
            alpha = max(
                alpha,
                best_value,
            )
        else:
            if value < best_value:
                best_value = value
                best_action = action
            beta = min(
                beta,
                best_value,
            )

    return best_action


# ============================================================
# Alpha Beta + Ordering Heuristic + Stats
# ============================================================
def alpha_beta_value_ordered_with_stats(
    game,
    state,
    alpha,
    beta,
    stats,
    depth=0,
):
    stats.nodes_visited += 1
    stats.max_depth = max(
        stats.max_depth,
        depth,
    )
    if game.terminal_test(state):
        stats.terminal_states += 1
        return game.utility(state)

    player = state[1]

    if player == "X":
        value = -inf

        for action in ordered_actions(
            game,
            state,
        ):
            value = max(
                value,
                alpha_beta_value_ordered_with_stats(
                    game,
                    game.result(
                        state,
                        action,
                    ),
                    alpha,
                    beta,
                    stats,
                    depth + 1,
                )
            )
            alpha = max(
                alpha,
                value,
            )
            if beta <= alpha:
                break

        return value
    else:
        value = inf

        for action in ordered_actions(
            game,
            state,
        ):
            value = min(
                value,
                alpha_beta_value_ordered_with_stats(
                    game,
                    game.result(
                        state,
                        action,
                    ),
                    alpha,
                    beta,
                    stats,
                    depth + 1,
                )
            )
            beta = min(
                beta,
                value,
            )
            if beta <= alpha:
                break

        return value