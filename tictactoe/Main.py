"""
Peyton Twigg

Uses pygame to create a tictactoe game that can be played between any combination of player types. The player types are
"child", which will just choose a random space; "teenager", which will choose any space unless the opponent could win on
the next move, in which case they will attempt to block; "adult", which uses minimax to choose the  most logical move;
"advanced adult", which uses minimax like the adult player, but with alpha-beta pruning; and a human player, which is
controlled by the user. Human players make a move by choosing any available square, and computer moves are initiated by
the user clicking anywhere on the board.
"""
import pygame
from Game import Game

# Get the user's preferences
print("Choose who will play as 'X'...")
while True:
    print("0 = Human Controlled")
    print("1 = Child")
    print("2 = Teenager")
    print("3 = Adult")
    print("4 = Enhanced Adult")
    player_X = input("\nEnter number: ")

    # User entered a valid number
    if player_X.isdigit() and int(player_X) in range(0,5):
        player_X = int(player_X)
        break
    # Invalid entry, try again
    else:
        print("\nPlease enter a valid number...")

print("Choose who will play as 'O'...")
while True:
    print("0 = Human Controlled")
    print("1 = Child")
    print("2 = Teenager")
    print("3 = Adult")
    print("4 = Enhanced Adult")
    player_O = input("\nEnter number: ")

    # User entered a valid number
    if player_O.isdigit() and int(player_O) in range(0,5):
        player_O = int(player_O)
        break
    # Invalid entry, try again
    else:
        print("\nPlease enter a valid number...")

player_types = ['Human', 'Child', 'Teenager', 'Adult', 'Enhanced Adult']

### Initialize pygame and its environment ###
game = Game(player_X, player_O)
pygame.init()
fps = 10
fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((480, 480))
playing = True
keep_playing = True
bg = (255, 255, 255)
lines = (0, 0, 0)

# Initialize the board for the game
game.setup_board()

# Set the window caption based on the player types
pygame.display.set_caption("TicTacToe: " + player_types[player_X] + " v. " + player_types[player_O])

# Main game loop
while playing:
    for event in pygame.event.get():
        # User clicked to close window
        if event.type == pygame.QUIT:
            playing = False
        # User has clicked on the screen
        elif event.type == pygame.MOUSEBUTTONUP:
            # If the game is still in progress, perform the next move
            if keep_playing:
                keep_playing = game.next_move(event)
            # Game is over, click the screen to exit
            else:
                playing = False

    # Redraw the board
    screen.fill(bg)
    game.board.draw(screen, lines, bg)
    pygame.display.flip()

print("PyGame is exiting...")
pygame.quit()
