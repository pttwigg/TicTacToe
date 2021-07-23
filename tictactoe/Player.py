from random import choice
from math import inf


# Base player class
class Player:
    def __init__(self, mark, opponent_mark):
        self.mark = mark
        self.opponent_mark = opponent_mark

    def make_move(self, board):
        pass


# Implements a kid who just picks any random spot
class Child(Player):
    def __init__(self, mark, opponent_mark):
        super().__init__(mark, opponent_mark)

    def make_move(self, board):
        # Just pick any open space
        return choice(board.open_spaces(board.state))


# Implements a player who tries to block if the opponent is about to win, else he just picks a random space
class Teenager(Player):
    def __init__(self, mark, opponent_mark):
        super().__init__(mark, opponent_mark)

    def make_move(self, board):
        # Go through each winning state to see if the opponent has filled 2/3 of any of them
        for win_state in board.winning_states:
            total = 0
            open_space = -1

            # Test the three spaces in the winning state
            for space in win_state:
                # Increment the number of spaces the opponent filled in that state
                if board.state[space] == self.opponent_mark:
                    total += 1
                # If the opponent did not fill a space, test if it is empty so it can be chosen
                elif board.state[space] == '-':
                    open_space = space

            # Opponent has filled 2 of 3 spaces, and the other is empty, so choose the empty space
            if total == 2 and open_space != -1:
                print("\nPlayer is about to win, blocking...\n")
                return open_space

        # The Opponent cannot win on the next turn, so randomly pick a spot
        print("\nNo block possible, placing randomly...\n")
        return choice(board.open_spaces(board.state))


# Implements a smart player that uses minimax
class Adult(Player):
    def __init__(self, mark, opponent_mark):
        super().__init__(mark, opponent_mark)

    def make_move(self, board):
        # Board is empty so pick a corner or the middle to start
        if len(board.open_spaces(board.state)) == 9:
            return choice([0,2,4,6,8])

        # Board is not empty, use minimax
        else:
            state_copy = board.state.copy()    # Create a copy of the board
            val = self.minimax(board, state_copy, len(board.open_spaces(board.state)), True)

            # Return the best move
            return val[1]

    # Minimax logic for finding the best move
    # Returns [value][best move]
    def minimax(self, board, node, depth, max_player):
        # This player has won
        if board.test_for_win(self.mark, node):
            return 1, -1
        # The opponent has won
        elif board.test_for_win(self.opponent_mark, node):
            return -1, -1
        # Draw
        elif depth == 0:
            return 0, -1

        # Maximizing player
        if max_player:
            best_value = -1
            best_move = -1

            # Try all the open spaces
            for child in board.open_spaces(node):
                new_node = node.copy()          # Make a new node
                new_node[child] = self.mark     # Add the new mark to the new node

                # Get the value of the best outcome for that move
                val = self.minimax(board, new_node, depth - 1, False)

                # Test whether this value is the best so far
                if best_value < val[0]:
                    best_value = val[0]
                    best_move = child       # Keep track of the best move

            return best_value, best_move

        # Minimizing player
        else:
            best_value = 1
            best_move = -1

            # Try all the open spaces
            for child in board.open_spaces(node):
                new_node = node.copy()                  # Make a new node
                new_node[child] = self.opponent_mark    # Add the new mark to the new node

                # Get the value of the best outcome for that move
                val = self.minimax(board, new_node, depth - 1, True)

                # Test whether this value is the best so far
                if val[0] < best_value:
                    best_value = val[0]
                    best_move = child       # Keep track of the best move

            return best_value, best_move


# Implements a smart player that uses alpha-beta pruning
class AdvancedAdult(Player):
    def __init__(self, mark, opponent_mark):
        super().__init__(mark, opponent_mark)

    def make_move(self, board):
        # Board is empty so pick a corner or the middle to start
        if len(board.open_spaces(board.state)) == 9:
            return choice([0,2,4,6,8])

        # Board is not empty, use minimax
        else:
            state_copy = board.state.copy()    # Create a copy of the board
            val = self.alpha_beta(board, state_copy, len(board.open_spaces(board.state)), -inf, +inf, True)

            # Return the best move
            return val[1]

    def alpha_beta(self, board, node, depth, a, b, max_player):
        # This player has won
        if board.test_for_win(self.mark, node):
            return 1, -1
        # The opponent has won
        elif board.test_for_win(self.opponent_mark, node):
            return -1, -1
        # Draw
        elif depth == 0:
            return 0, -1

        # Maximizing player
        if max_player:
            value = -inf
            best_move = -1      # Initialize to no best move

            # Try all the open spaces
            for child in board.open_spaces(node):
                new_node = node.copy()          # Make a new node
                new_node[child] = self.mark     # Add the new mark to the new node

                # Get the value of the best outcome for that move
                alpha_beta = self.alpha_beta(board, new_node, depth - 1, a, b, False)

                # Test if the value is the best so far
                if value < alpha_beta[0]:
                    value = alpha_beta[0]
                    best_move = child

                # Update the alpha value if it is higher
                a = max(a, value)

                # Break if there is no reason to go further
                if a >= b:
                    break

            return value, best_move

        # Minimizing player
        else:
            value = +inf
            best_move = -1      # Initialize to no best move

            # Try all the open spaces
            for child in board.open_spaces(node):
                new_node = node.copy()                  # Make a new node
                new_node[child] = self.opponent_mark    # Add the new mark to the new node

                # Get the value of the best outcome for that move
                alpha_beta = self.alpha_beta(board, new_node, depth - 1, a, b, True)

                # Test if the value is the best so far
                if alpha_beta[0] < value:
                    value = alpha_beta[0]
                    best_move = child

                # Update the beta value if it is lower
                b = min(b, value)

                # Break if there is no reason to go further
                if b <= a:
                    break

            return value, best_move
