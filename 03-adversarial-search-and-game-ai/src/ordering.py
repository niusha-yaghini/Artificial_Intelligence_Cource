# Ordering is an independent heuristic.

CENTER_FIRST_ORDER = [
    4,
    0,
    2,
    6,
    8,
    1,
    3,
    5,
    7,
]

def ordered_actions(
    game,
    state,
):
    actions = list(
        game.actions(state)
    )
    return sorted(
        actions,
        key=lambda action:
            CENTER_FIRST_ORDER.index(action)
    )