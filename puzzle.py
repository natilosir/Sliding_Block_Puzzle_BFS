import \
    time
from collections import \
    deque


class PuzzleState:
    def __init__(
            self,
            board,
            size,
            parent=None,
            move=None,
            depth=0):
        self.board = [
            row[
            :]
            for
            row
            in
            board]
        self.size = size
        self.parent = parent
        self.move = move
        self.depth = depth
        self.blank_pos = self.find_blank()

    def find_blank(
            self):
        for i in range(
                self.size):
            for j in range(
                    self.size):
                if \
                self.board[
                    i][
                    j] == 0:
                    return (
                    i,
                    j)

    def get_possible_moves(
            self):
        moves = []
        i, j = self.blank_pos

        if i > 0:
            moves.append(
                'UP')
        if i < self.size - 1:
            moves.append(
                'DOWN')
        if j > 0:
            moves.append(
                'LEFT')
        if j < self.size - 1:
            moves.append(
                'RIGHT')

        return moves

    def move_blank(
            self,
            direction):
        i, j = self.blank_pos
        new_board = [
            row[
            :]
            for
            row
            in
            self.board]

        if direction == 'UP' and i > 0:
            new_board[
                i][
                j], \
            new_board[
                i - 1][
                j] = \
            new_board[
                i - 1][
                j], \
            new_board[
                i][
                j]
        elif direction == 'DOWN' and i < self.size - 1:
            new_board[
                i][
                j], \
            new_board[
                i + 1][
                j] = \
            new_board[
                i + 1][
                j], \
            new_board[
                i][
                j]
        elif direction == 'LEFT' and j > 0:
            new_board[
                i][
                j], \
            new_board[
                i][
                j - 1] = \
            new_board[
                i][
                j - 1], \
            new_board[
                i][
                j]
        elif direction == 'RIGHT' and j < self.size - 1:
            new_board[
                i][
                j], \
            new_board[
                i][
                j + 1] = \
            new_board[
                i][
                j + 1], \
            new_board[
                i][
                j]
        else:
            return None

        return PuzzleState(
            new_board,
            self.size,
            self,
            direction,
            self.depth + 1)

    def is_goal(
            self):
        goal = [
            [
                0,
                1,
                2],
            [
                3,
                4,
                5],
            [
                6,
                7,
                8]]
        return self.board == goal

    def __eq__(
            self,
            other):
        return self.board == other.board

    def __hash__(
            self):
        return hash(
            str(self.board))


def solve_puzzle(
        initial_state):
    queue = deque()
    queue.append(
        initial_state)
    visited = set()
    visited.add(
        initial_state)

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            path = []
            while current_state.parent:
                path.append(
                    current_state.move)
                current_state = current_state.parent
            return path[
                   ::-1]

        for move in current_state.get_possible_moves():
            new_state = current_state.move_blank(
                move)
            if new_state and new_state not in visited:
                visited.add(
                    new_state)
                queue.append(
                    new_state)

    return None


def print_solution(
        initial_state,
        solution):
    current = initial_state
    print(
        "\ninitial state:")
    for row in current.board:
        print(
            row)

    for step, move in enumerate(
            solution,
            1):
        current = current.move_blank(
            move)
        print(
            f"\n{step}: {move}")
        for row in current.board:
            print(
                row)

    print(
        "\nFinal solution:")
    for row in current.board:
        print(row)
    print(
        "Is Goal?",
        current.is_goal())



test_board =  [[1, 3, 6],
    [5, 0, 2],
    [4, 7, 8]]
initial_state = PuzzleState(
    test_board,
    3)

solution = solve_puzzle(
    initial_state)

if solution:
    print(
        "\nroad map:")
    for step, move in enumerate(
            solution,
            1):
        print(
            f"{step}. {move}")

    print_solution(
        initial_state,
        solution)
else:
    print(
        "not found")


time.sleep(100)