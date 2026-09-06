# Game State Abstraction:
# That is, the Minimax algorithm does not need to know what the game is.

# Every game should have these functions:
#     1) Initial State
#     2) Actions
#     3) Result
#     4) Terminal Test
#     5) Utility


# ============================================================
# Total Game Structure
# ============================================================
from abc import ABC, abstractmethod


class Game(ABC):

    @abstractmethod
    def initial_state(self):
        pass

    @abstractmethod
    def actions(self, state):
        pass

    @abstractmethod
    def result(self, state, action):
        pass

    @abstractmethod
    def terminal_test(self, state):
        pass

    @abstractmethod
    def utility(self, state):
        pass
    
    
# ============================================================
# Tic-Tac-Toe Game
# ============================================================
class TicTacToe(Game):
    def __init__(self):
        self.empty = " "

        self.winning_lines = [
            (0,1,2),
            (3,4,5),
            (6,7,8),

            (0,3,6),
            (1,4,7),
            (2,5,8),

            (0,4,8),
            (2,4,6),
        ]
        
    def initial_state(self):
        board = (
            self.empty,
        ) * 9
        
        return (
            board,
            # This only determines which player starts the game.
            "X",
        )
        
    def actions(
        self,
        state,
    ):
        board, _ = state

        return [
            index
            for index, value in enumerate(board)
            if value == self.empty
        ]
        
    def result(
        self,
        state,
        action,
    ):
        board, player = state
        new_board = list(board)
        new_board[action] = player

        next_player = (
            "O"
            if player == "X"
            else "X"
        )

        return (
            tuple(new_board),
            next_player,
        )
        
    def winner(self, board):
        for line in self.winning_lines:
            a,b,c = line

            if (
                board[a] != self.empty
                and
                board[a] == board[b]
                and
                board[b] == board[c]
            ):
                return board[a]

        return None
    
    def terminal_test(
        self,
        state,
    ):
        board, _ = state

        return (
            self.winner(board) is not None
            or
            self.empty not in board
        )
        
    def utility(
        self,
        state,
    ):
        board, _ = state
        winner = self.winner(board)

        if winner == "X":
            return 10000

        if winner == "O":
            return -10000

        return 0
