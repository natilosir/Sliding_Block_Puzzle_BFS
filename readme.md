# 48-Puzzle Solver

This Python program solves the classic 8-puzzle game using a Breadth-First Search (BFS) algorithm. The puzzle consists of a 3x3 grid with 8 numbered tiles and one blank space. The goal is to rearrange the tiles from a given initial state to the goal state by sliding them into the blank space.

## Features

- **BFS Algorithm**: Uses BFS to explore all possible moves level by level, guaranteeing the shortest solution path.
- **PuzzleState Class**: Represents each state of the puzzle, including the board configuration, blank position, and possible moves.
- **Interactive Solution Display**: Prints each move step-by-step, showing the board configuration after each move.

## How It Works

1. **Initialization**: The program starts with a predefined initial board state.
2. **Solving**: The BFS algorithm explores all possible moves from the initial state, avoiding revisiting any state.
3. **Solution Path**: Once the goal state is reached, the solution path (sequence of moves) is reconstructed and displayed.

## Code Structure

- **PuzzleState**: Handles the puzzle board, blank position, possible moves, and state transitions.
- **solve_puzzle**: Implements BFS to find the shortest path to the goal state.
- **print_solution**: Displays the solution step-by-step, including the board after each move.

## Example

### Initial Board:
```bash
[1, 3, 6]
[5, 0, 2]
[4, 7, 8]
```

### Solution Steps:
1. **UP**: Move the blank space up.
2. **LEFT**: Move the blank space left.
3. ... (continues until the goal state is reached).

### Goal State:
```bash
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]
```

## Usage

1. Modify the `test_board` variable in the script to set a custom initial state.
2. Run the script: `py puzzle.py`.
3. The solution path and intermediate states will be printed in the console.

## Requirements

- Python 3.x
- No external dependencies are required.

## Notes

- The program includes a 10-second delay (`time.sleep(10)`) at the end to allow users to view the output before the console closes (useful when running the script in some environments).
- The goal state is hardcoded as:
```bash
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]
```