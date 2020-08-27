import sys
import argparse
from typing import List

from util import generate_snail_positions

def make_ordered_puzzle(puzzle_size: int) -> List[List[int]]:
    puzzle = [[0 for _ in range(puzzle_size)] for _ in range(puzzle_size)]
    correct_values = [val for val in range(1, puzzle_size)] + [0]
    for (x, y), value in zip(generate_snail_positions(puzzle_size), correct_values):
        empty_puzzle[x][y] = value
    return puzzle

def make_puzzle(puzzle_size: int, solvable: bool, suffle_iterations: int) -> List[List[int]]:
    ordered_puzzle = make_ordered_puzzle(puzzle_size)
    print(ordered_puzzle)

def print_puzzle_header(puzzle_size:int) -> None:
    print(puzzle_size)
    print("-----------")

def print_puzzle_body(puzzle_size:int) -> None:
    pass
    w = len(str(puzzle_size * puzzle_size))
    for y in range(s):
        for x in range(s):
            print("{:s} ".format((str(puzzle[x + y * s]).rjust(w))), end="")
        print("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("size", type=int, help="Size of the puzzle's side. Must be >3.")
    parser.add_argument("-u", "--unsolvable", action="store_true", default=False,
                        help="Forces generation of an unsolvable puzzle")
    parser.add_argument("-i", "--iterations", type=int, default=10000, help="Number of passes")

    args = parser.parse_args()

    random.seed()

    if args.size < 3:
        print("Can't generate a puzzle with size lower than 2. It says so in the help. Dummy.")
        sys.exit(1)

    puzzle_size = args.size

    solvable = not args.unsolvable
    puzzle = make_puzzle(puzzle_size, solvable=solvable, iterations=args.iterations)

    
    print_puzzle_header()
    print_puzzle_body()
