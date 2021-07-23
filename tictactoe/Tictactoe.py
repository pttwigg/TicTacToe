import pygame


class Board:
    def __init__(self):
        # List of the coords for each box
        self.coords = [(0, 0),   (160, 0),   (320, 0),
                       (0, 160), (160, 160), (320, 160),
                       (0, 320), (160, 320), (320, 320)]

        # List of each winning state
        self.winning_states = [(0,1,2), (3,4,5), (6,7,8), (0,4,8),
                               (0,3,6), (1,4,7), (2,5,8), (2,4,6)]

        # Array for the board state.
        self.state = []

        # Holds the spaces for the board
        self.spaces = []

        # Initialize the state and the pegs
        for space in range(9):
            self.spaces.append(Space(self.coords[space], space))
            self.state.append('-')

    # Print out the current board state
    def print_state(self):
        for space in range(3):
            print(self.state[space], end=" ")
        print()

        for space in range(3, 6):
            print(self.state[space], end=" ")
        print()

        for space in range(6, 9):
            print(self.state[space], end=" ")
        print()
        print()

    # Return a list of all open spaces on the board
    @staticmethod
    def open_spaces(state):
        open_spaces = []
        for space in range(9):
            if state[space] == '-':
                open_spaces.append(space)
        return open_spaces

    # Test to see if a player has won
    def test_for_win(self, mark, state):
        for i in self.winning_states:
            if  state[i[0]] == mark \
            and state[i[1]] == mark \
            and state[i[2]] == mark:

                return True
        return False

    # Draw the board including the spaces
    def draw(self, screen, line_color, bg_color):
        # Background color
        screen.fill(bg_color)

        # Draw the lines
        pygame.draw.line(screen, line_color, (159, 0), (159, 480), 5)
        pygame.draw.line(screen, line_color, (319, 0), (319, 480), 5)
        pygame.draw.line(screen, line_color, (0, 159), (480, 159), 5)
        pygame.draw.line(screen, line_color, (0, 319), (480, 319), 5)

        # Draw the space markers
        for space in range(9):
            self.spaces[space].draw(screen, self.state[space])


class Space:
    def __init__(self, location, space_num):
        self.space_num = space_num
        self.imageX = pygame.image.load("X.png").convert_alpha()  # Load the X
        self.imageO = pygame.image.load("O.png").convert_alpha()  # Load the O
        self.rect = pygame.Rect(location, (160, 160))

    # Draw the mark onto the screen
    def draw(self, screen, mark):
        if mark == 'X':
            screen.blit(self.imageX, self.rect)
        elif mark == 'O':
            screen.blit(self.imageO, self.rect)
