# 8-Puzzle Solver

An implementation of the classic 8-puzzle problem solver using both A* and BFS algorithms.

## Features

- Solves 8-puzzle problems using:
    - A* algorithm with Manhattan distance heuristic
    - Breadth-First Search (BFS)
- Displays each move and the puzzle state after the move
- Measures and reports solution time
- Supports both console output and file output

## Requirements

- Python 3.x

## Installation

No installation required. Just download the `puzzle.py` file.

## Usage

### Basic Command

```py
python puzzle.py [--astar|--bfs] input_file.txt
```

### Arguments
- `--astar`: Use A* search algorithm

- `--bfs`: Use Breadth-First Search algorithm

- `input_file.txt`: Path to input file containing the puzzle

### Input File Format
The input file should contain the initial puzzle state in one of these formats:

1. With size specification (recommended):

```bash
3
1 2 3
4 5 6
7 8 0
```
2. Without size specification (assumes 3x3):

```bash
1 2 3
4 5 6
7 8 0
```
- Use `0` to represent the empty tile
- Numbers should be space-separated
- Each row on a new line

## Output
### The program will:

1. Print the solution steps with puzzle states to the console
1. Save detailed solution to [input_filename]_solution.txt

### Example
Input file puzzle.txt:

```bash
3
1 2 5
3 4 8
6 7 0
```
Command:

```bash
python puzzle.py --astar puzzle.txt
```
Console output will show each move and puzzle state:

```bash
Step 1: UP
1 2 5
3 4 .
6 7 8

Step 2: LEFT
1 2 .
3 4 5
6 7 8
...
```
And save complete solution to `puzzle_solution.txt`.

---
## Algorithms

- A*
- - Generally faster for solvable puzzles.
- - Finds good (but not always shortest) solutions.
- - Uses Manhattan distance heuristic.

- BFS
- - Guaranteed to find the shortest solution.
- - May be slower for complex puzzles.
- - Uses more memory for large search spaces.

---

## Notes
- The program only supports **3x3 puzzles**.
- Unsolvable puzzles will be detected (no solution found).
- Empty tile is displayed as `.` in output.
- Solution file includes timing and step count information.
