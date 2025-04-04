import sys
import time
import heapq
from collections import deque

class PuzzleState:
    def __init__(self, board, size, parent=None, move=None, depth=0):
        self.board = [row[:] for row in board]
        self.size = size
        self.parent = parent
        self.move = move
        self.depth = depth
        self.blank_pos = self.find_blank()
        self.cost = self.depth + self.manhattan_distance()

    def find_blank(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)

    def get_possible_moves(self):
        moves = []
        i, j = self.blank_pos

        if i > 0:
            moves.append('UP')
        if i < self.size - 1:
            moves.append('DOWN')
        if j > 0:
            moves.append('LEFT')
        if j < self.size - 1:
            moves.append('RIGHT')

        return moves

    def move_blank(self, direction):
        i, j = self.blank_pos
        new_board = [row[:] for row in self.board]

        if direction == 'UP' and i > 0:
            new_board[i][j], new_board[i - 1][j] = new_board[i - 1][j], new_board[i][j]
        elif direction == 'DOWN' and i < self.size - 1:
            new_board[i][j], new_board[i + 1][j] = new_board[i + 1][j], new_board[i][j]
        elif direction == 'LEFT' and j > 0:
            new_board[i][j], new_board[i][j - 1] = new_board[i][j - 1], new_board[i][j]
        elif direction == 'RIGHT' and j < self.size - 1:
            new_board[i][j], new_board[i][j + 1] = new_board[i][j + 1], new_board[i][j]
        else:
            return None

        return PuzzleState(new_board, self.size, self, direction, self.depth + 1)

    def is_goal(self):
        goal = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        return self.board == goal

    def manhattan_distance(self):
        distance = 0
        goal_positions = {
            0: (0, 0),
            1: (0, 1),
            2: (0, 2),
            3: (1, 0),
            4: (1, 1),
            5: (1, 2),
            6: (2, 0),
            7: (2, 1),
            8: (2, 2)
        }
        
        for i in range(self.size):
            for j in range(self.size):
                value = self.board[i][j]
                if value != 0:
                    goal_i, goal_j = goal_positions[value]
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __lt__(self, other):
        return self.cost < other.cost

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else "." for num in row))
        print()

def solve_puzzle_astar(initial_state):
    open_list = []
    heapq.heappush(open_list, initial_state)
    visited = set()
    visited.add(initial_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            path = []
            while current_state.parent:
                path.append(current_state.move)
                current_state = current_state.parent
            return path[::-1]

        for move in current_state.get_possible_moves():
            new_state = current_state.move_blank(move)
            if new_state and new_state not in visited:
                visited.add(new_state)
                heapq.heappush(open_list, new_state)

    return None

def solve_puzzle_bfs(initial_state):
    queue = deque()
    queue.append(initial_state)
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            path = []
            while current_state.parent:
                path.append(current_state.move)
                current_state = current_state.parent
            return path[::-1]

        for move in current_state.get_possible_moves():
            new_state = current_state.move_blank(move)
            if new_state and new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

    return None

def read_board_from_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        
        try:
            size = int(lines[0])
            start_line = 1
        except ValueError:
            size = 3
            start_line = 0
            
        board = []
        for line in lines[start_line:start_line+size]:
            row = [int(num) for num in line.split()]
            if len(row) != size:
                raise ValueError(f"Each row must have exactly {size} numbers")
            board.append(row)
        
        return board, size

def write_solution_to_file(input_filename, initial_state, solution, algorithm, time_taken):
    if '.' in input_filename:
        base, ext = input_filename.rsplit('.', 1)
        output_filename = f"{base}_solution.{ext}"
    else:
        output_filename = f"{input_filename}_solution"
    
    with open(output_filename, 'w') as file:
        if not solution:
            file.write("No solution found.\n")
            return
        
        file.write(f"Algorithm: {algorithm}\n")
        file.write(f"Time taken: {time_taken:.4f} seconds\n")
        file.write(f"Steps: {len(solution)}\n\n")
        
        file.write("Initial state:\n")
        for row in initial_state.board:
            file.write(" ".join(str(num) if num != 0 else "." for num in row) + "\n")
        file.write("\n")
        
        current = initial_state
        for step, move in enumerate(solution, 1):
            current = current.move_blank(move)
            file.write(f"Step {step}: {move}\n")
            for row in current.board:
                file.write(" ".join(str(num) if num != 0 else "." for num in row) + "\n")
            file.write("\n")
        
        file.write(f"Solved in {len(solution)} steps\n")

def print_solution(initial_state, solution):
    print("\nInitial state:")
    initial_state.print_board()
    
    current = initial_state
    for step, move in enumerate(solution, 1):
        current = current.move_blank(move)
        print(f"Step {step}: {move}")
        current.print_board()
    
    print(f"Solved in {len(solution)} steps")

def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ["--astar", "--bfs"]:
        print("Usage: python puzzle.py [--astar|--bfs] input_file.txt")
        return
    
    algorithm = sys.argv[1][2:]  # 'astar' or 'bfs'
    input_file = sys.argv[2]
    
    try:
        board, size = read_board_from_file(input_file)
        if size != 3:
            print("Note: This implementation currently only supports 3x3 puzzles")
            return
        
        initial_state = PuzzleState(board, size)
        
        start_time = time.time()
        
        if algorithm == "astar":
            solution = solve_puzzle_astar(initial_state)
        else:  # bfs
            solution = solve_puzzle_bfs(initial_state)
        
        end_time = time.time()
        time_taken = end_time - start_time
        
        if solution:
            print(f"\nSolution found using {algorithm.upper()}:")
            print_solution(initial_state, solution)
            print(f"\nTime taken: {time_taken:.4f} seconds")
        else:
            print("No solution found.")
        
        write_solution_to_file(input_file, initial_state, solution, algorithm, time_taken)
        output_file = input_file.replace('.txt', '_solution.txt') if input_file.endswith('.txt') else input_file + '_solution'
        print(f"\nSolution written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError as e:
        print(f"Error in input file: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()