import os
import random
import time

# Game constants
WIDTH = 10
HEIGHT = 10
PACMAN = 'P'
DOT = '.'
WALL = '#'
EMPTY = ' '

def initialize_board():
    """Initialize the game board with walls, dots, and an empty space for Pac-Man."""
    board = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    # Add walls
    for i in range(WIDTH):
        board[0][i] = WALL
        board[HEIGHT-1][i] = WALL
    for i in range(HEIGHT):
        board[i][0] = WALL
        board[i][WIDTH-1] = WALL

    # Add dots
    for _ in range(10):
        x = random.randint(1, WIDTH-2)
        y = random.randint(1, HEIGHT-2)
        if board[y][x] == EMPTY:
            board[y][x] = DOT

    return board

def print_board(board, pacman_x, pacman_y):
    """Print the game board with Pac-Man's position."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == pacman_x and y == pacman_y:
                print(PACMAN, end=' ')
            else:
                print(board[y][x], end=' ')
        print()
    print()

def move_pacman(pacman_x, pacman_y, direction, board):
    """Move Pac-Man based on direction and update the board."""
    new_x, new_y = pacman_x, pacman_y

    if direction == 'w':  # Move up
        new_y -= 1
    elif direction == 's':  # Move down
        new_y += 1
    elif direction == 'a':  # Move left
        new_x -= 1
    elif direction == 'd':  # Move right
        new_x += 1

    if board[new_y][new_x] != WALL:
        pacman_x, pacman_y = new_x, new_y
        if board[pacman_y][pacman_x] == DOT:
            board[pacman_y][pacman_x] = EMPTY
    return pacman_x, pacman_y

def pacman_game():
    board = initialize_board()
    pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2  # Start Pac-Man in the center

    while True:
        print_board(board, pacman_x, pacman_y)
        direction = input("Move (w/a/s/d): ").strip().lower()
        if direction in ['w', 'a', 's', 'd']:
            pacman_x, pacman_y = move_pacman(pacman_x, pacman_y, direction, board)
        else:
            print("Invalid input. Use 'w', 'a', 's', or 'd'.")

        # Check if there are any dots left
        if all(board[y][x] != DOT for y in range(1, HEIGHT-1) for x in range(1, WIDTH-1)):
            print("Congratulations! You collected all the dots.")
            break

        time.sleep(0.2)  # Slow down the game loop

if __name__ == "__main__":
    pacman_game()
