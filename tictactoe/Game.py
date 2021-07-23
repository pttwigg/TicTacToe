import Tictactoe
import Player


class Game:
    def __init__(self, player_X, player_O):
        self.turn_num = 0
        self.turns = "XOXOXOXOX"    # String to keep track of turns
        self.gameover = False

        self.player_X_type = player_X
        self.player_O_type = player_O

        # Initialize the player type the user chose for X
        if self.player_X_type == 0:
            self.player_X = Player.Player('X', 'O')     # Human player
        elif self.player_X_type == 1:
            self.player_X = Player.Child('X', 'O')
        elif self.player_X_type == 2:
            self.player_X = Player.Teenager('X', 'O')
        elif self.player_X_type == 3:
            self.player_X = Player.Adult('X', 'O')
        elif self.player_X_type == 4:
            self.player_X = Player.AdvancedAdult('X', 'O')

        # Initialize the player type the user chose for O
        if self.player_O_type == 0:
            self.player_O = Player.Player('O', 'X')     # Human player
        elif self.player_O_type == 1:
            self.player_O = Player.Child('O', 'X')
        elif self.player_O_type == 2:
            self.player_O = Player.Teenager('O', 'X')
        elif self.player_O_type == 3:
            self.player_O = Player.Adult('O', 'X')
        elif self.player_O_type == 4:
            self.player_O = Player.AdvancedAdult('O', 'X')

        # Print the initial turn
        if self.player_X_type == 0:
            print("\nX's turn.")
            print("Choose a space...\n")
        else:
            print("\nComputer player X's turn.")
            print("Click anywhere to show move...\n")

    # Initializes the board and spaces
    # Must be done after initializing the pygame screen in order to load images
    def setup_board(self):
        # Initialize the board
        self.board = Tictactoe.Board()

    # Gets the move for a human player
    def get_user_move(self, event, mark):
        pos = event.pos

        # Go through each space to see if it was clicked on
        for space in range(9):
            # Space was clicked on
            if self.board.spaces[space].rect.collidepoint(pos):
                # Redo move if the space was already occupied
                if self.board.state[space] != '-':
                    print("Illegal move, please choose an unoccupied space...")
                    return True

                # Update the space with the correct mark
                self.board.state[space] = mark

                # Test if the player won
                self.gameover = self.board.test_for_win(mark, self.board.state)

                if self.gameover:
                    print("\n" + mark + " wins the game!!!")
                    print("Click anywhere to exit...")

    # Perform the next move in the game.
    def next_move(self, event):
        # X's turn
        if self.turns[self.turn_num] == 'X':
            # Human player's turn
            if self.player_X_type == 0:
                # Returns True if the move was invalid
                if self.get_user_move(event, 'X'):
                    return True
            # Computer player's turn
            else:
                # Have the opponent make a move, and update the game state
                self.board.state[self.player_X.make_move(self.board)] = 'X'

                # Test if the opponent has won
                self.gameover = self.board.test_for_win('X', self.board.state)

                if self.gameover:
                    print("\nX wins the game!!!")
                    print("Click anywhere to exit...")

        elif self.turns[self.turn_num] == 'O':
            # Human player's turn
            if self.player_O_type == 0:
                # Returns True if the move was invalid
                if self.get_user_move(event, 'O'):
                    return True

            # Computer player's turn
            else:
                # Have the opponent make a move, and update the game state
                self.board.state[self.player_O.make_move(self.board)] = 'O'

                # Test if the opponent has won
                self.gameover = self.board.test_for_win('O', self.board.state)

                if self.gameover:
                    print("\nO wins the game!!!")
                    print("Click anywhere to exit...")

        self.turn_num += 1
        self.board.print_state()

        # Test for draw
        if self.turn_num == 9 and not self.gameover:
            print("Draw...")
            print("Click anywhere to exit...\n")
            return False

        # Show the next turn if there is another
        if not self.gameover:
            # X's turn next
            if self.turns[self.turn_num] == 'X':
                # Human player's turn
                if self.player_X_type == 0:
                    print("Human player X's turn.")
                    print("Choose a space...\n")
                # Computer player's turn
                else:
                    print("Computer player X's turn.")
                    print("Click anywhere to show next move...\n")
            # O's turn next
            else:
                # Human player's turn
                if self.player_O_type == 0:
                    print("Human player O's turn.")
                    print("Choose a space...\n")
                # Computer player's turn
                else:
                    print("Computer player O's turn.")
                    print("Click anywhere to show next move...\n")

        # Return true as long as nobody has won
        return not self.gameover
