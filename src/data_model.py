import logging
import copy
from dataclasses import dataclass
from typing import List, Any, Dict
from util import generate_snail_positions, flatten_nested_list, colors


@dataclass
class PuzzleSolution:
    "contains the finished state and a map to get locations of each digits."
    state: List[List[int]]
    positions: Dict


@dataclass
class ParsingError(Exception):
    message: str


# Dataclass decorator implements for me magic methods (__init__ , __eq__ , ....)
@dataclass(order=True)
class PuzzleState:
    overall_cost: int
    moveNumber: int
    heuristicCost: int
    size: int
    currentState: List[List[int]]
    previous_state: Any

    def hash(self):
        to_str = [str(x) for x in flatten_nested_list(self.currentState)]
        joined = "".join(to_str)
        return int(joined)

    def is_final_state(self, solution):
        return self.currentState == solution

    def expand(self):
        "generates possible transitions from a given state"

        for child in generate_permutations(self):
            # child.display()
            child.previous_state = self
            child.moveNumber = self.moveNumber + 1
            child.size = self.size
            yield child

    def compute_cost(self, solution, heuristic, search_type):
        "Take a heuristic function as param to compute cost."
        # Greedy only uses heuristic
        if search_type == "greedy":
            self.heuristicCost = heuristic(self, solution)
            self.overall_cost = self.heuristicCost
        # uniform cost is Breadth First Search algo.
        elif search_type == "uniform":
            self.overall_cost = self.moveNumber
        else:
            self.heuristicCost = heuristic(self, solution)
            self.overall_cost = self.heuristicCost + self.moveNumber

    def display_solution(self, stats):
        self.display_move_number()
        self.display_path()
        self.display_analytics(stats)

    def display_move_number(self):
        print("\n\t\t SOLUTION :\n")
        print(f"Number of moves to solve the puzzle : {self.moveNumber}\n")

    def display_path(self):
        "recursively print path to solve puzzle"
        if self.previous_state:
            self.previous_state.display_path()
        self.display()

    def display_analytics(self, stats):
        print("\t\t STATS :\n")
        print(f"Total node selected in open list : {stats.expanded_node_number}")
        print(
            f"Maximum amount of nodes in open list at same time: {stats.total_node_number}\n"
        )

    def display(self):
        "display current state of puzzle on screen"
        width = self.size // 2
        for elem in self.currentState:
            print("[", end="")
            for item in elem[:-1]:
                if item == 0:
                    print(colors.OKGREEN, end="")
                    print(f"{item:{width}}", end="")
                    print(f"{colors.ENDC}, ", end="")
                else:
                    print(f"{item:{width}}, ", end="")

            # print(f"{elem[-1]:{width}}]", end="\n\n")

            if elem[-1] == 0:
                print(colors.OKGREEN, end="")
                print(f"{elem[-1]:{width}}", end="")
                print(f"{colors.ENDC}]")
            else:
                print(f"{elem[-1]:{width}}]")
        print("")


def generate_permutations(puzzle):
    for (empty_tile_pos, swap_tile_pos) in get_allowed_permutations(
        puzzle.currentState
    ):
        logging.debug(f"empty position : {empty_tile_pos}")
        logging.debug(f"tile to switch position : {swap_tile_pos}")
        new_puzzle = permute_puzzle(puzzle.currentState, empty_tile_pos, swap_tile_pos)
        yield new_puzzle


def get_allowed_permutations(puzzle):
    (y, x) = get_empty_position(puzzle)
    if y > 0:
        yield ((y, x), (y - 1, x))
    if y < len(puzzle) - 1:
        yield ((y, x), (y + 1, x))
    if x > 0:
        yield ((y, x), (y, x - 1))
    if x < len(puzzle) - 1:
        yield ((y, x), (y, x + 1))


def get_empty_position(puzzle):
    for x in range(len(puzzle)):
        for y in range(len(puzzle)):
            if puzzle[y][x] == 0:
                return (y, x)


def permute_puzzle(puzzle, empty_tile_pos, swap_tile_pos):
    puzzle_copy = copy.deepcopy(puzzle)
    new = PuzzleState(0, 0, 0, 0, puzzle_copy, 0)
    new.currentState[empty_tile_pos[0]][empty_tile_pos[1]] = new.currentState[
        swap_tile_pos[0]
    ][swap_tile_pos[1]]
    new.currentState[swap_tile_pos[0]][swap_tile_pos[1]] = 0
    return new


def generate_puzzle_solution(size):
    puzzle = [[0 for _ in range(size)] for _ in range(size)]
    solution = PuzzleSolution(puzzle, {})

    for ((x, y), num) in zip(generate_snail_positions(size), range(1, size * size + 1)):
        # last turn number must be zero (empty tile)
        if num == size * size:
            num = 0
        solution.state[y][x] = num
        solution.positions[num] = (y, x)
    return solution
