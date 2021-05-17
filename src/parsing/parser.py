import sys
import re
import logging
from typing import List
from data_model import PuzzleState
from parsing.integrity import check_puzzle_integrity


def line_is_comment(line: str) -> bool:
    trimmed_line = line.lstrip()
    if trimmed_line.startswith("#") or trimmed_line.startswith("-"):
        logging.debug("Comment")
        return True
    return False


def line_is_puzzle_size(line: str) -> bool:
    trimmed_line = line.strip()
    if re.match(r"\d+(\s+)?(#.*)?$", trimmed_line):
        return True
    return False


def line_is_puzzle_content(line, puzzle_size) -> bool:
    trimmed_line = line.strip()
    if re.match(fr"(\d+\s+){ {puzzle_size-1} }(\d+\s*)(#.*)?$", trimmed_line):
        return True
    logging.warning(f"line should contain {puzzle_size} numbers")
    return False


def get_puzzle_size(line: str) -> int:
    "Return puzzle size as an int."
    return int(line.split()[0])


def get_puzzle_row(puzzle_size: int, line: str) -> List[int]:
    splitted_line = line.split()
    row_string = splitted_line[0:puzzle_size]
    return [int(x) for x in row_string]


def parse_input() -> PuzzleState:
    logging.debug("Parsing Input")
    # default value before parsing actual value.
    puzzle = PuzzleState(0, 0, 0, 0, [], 0)
    rows = []
    for line in sys.stdin:
        if line_is_comment(line):
            continue
        if not puzzle.size and line_is_puzzle_size(line):
            puzzle.size = get_puzzle_size(line)
        elif puzzle.size and line_is_puzzle_content(line, puzzle.size):
            row = get_puzzle_row(puzzle.size, line)
            rows.append(row)
    puzzle.current_state = rows
    return puzzle


def parse_stdin() -> PuzzleState:
    puzzle = parse_input()
    check_puzzle_integrity(puzzle)
    return puzzle
