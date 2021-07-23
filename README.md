# tictactoe
Tictactoe game written in python using pygame.

The game can be played between any combination of 5 player types.
- Child: Picks a random space
- Teenager: Chooses a random space unless the opponent is about to win, in which case will attempt to block
- Adult: Uses minimax algorithm in order to find the most logical next move
- Advanced Adult: Same as adult, but uses alpha-beta pruning
- Human: User controlled player

The user will pick the players for X and O in the console, and the board will open in a new window. Any human-controlled player's moves are made by clicking on any available space on the screen. Computer controlled player moves are initiated by clicking anywhere on the screen.
