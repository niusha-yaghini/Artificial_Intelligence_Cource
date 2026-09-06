def evaluate_tic_tac_toe(
    game,
    state,
):
    board, _ = state
    score = 0

    for line in game.winning_lines:
        values = [
            board[i]
            for i in line
        ]

        if values.count("X") == 3:
            score += 100
        elif values.count("X") == 2 and values.count(" ") == 1:
            score += 10
        elif values.count("X") == 1 and values.count(" ") == 2:
            score += 1

        if values.count("O") == 3:
            score -= 100
        elif values.count("O") == 2 and values.count(" ") == 1:
            score -= 10
        elif values.count("O") == 1 and values.count(" ") == 2:
            score -= 1

    return score


def count_immediate_wins(
    game,
    state,
    player,
):
    wins = 0
    board, current_player = state
    for action in game.actions(state):
        new_state = (
            game.result(
                (
                    board,
                    player,
                ),
                action,
            )
        )

        if game.terminal_test(new_state):
            if game.utility(new_state) > 0 and player == "X":
                wins += 1
            elif game.utility(new_state) < 0 and player == "O":

                wins += 1

    return wins


def evaluate_tic_tac_toe_v2(
    game,
    state,
):
    board, _ = state

    # Terminal states
    if game.terminal_test(state):
        return game.utility(state) * 10000

    score = 0

    # Immediate threats
    x_wins = count_immediate_wins(
        game,
        state,
        "X",
    )
    o_wins = count_immediate_wins(
        game,
        state,
        "O",
    )

    score += x_wins * 1000
    score -= o_wins * 1000

    # Line evaluation
    for line in game.winning_lines:
        values = [
            board[i]
            for i in line
        ]

        if values.count("X") == 2 and values.count(" ") == 1:
            score += 10
        elif values.count("O") == 2 and values.count(" ") == 1:
            score -= 10
        elif values.count("X") == 1 and values.count(" ") == 2:
            score += 1
        elif values.count("O") == 1 and values.count(" ") == 2:
            score -= 1

    return score