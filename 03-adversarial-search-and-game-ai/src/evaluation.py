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