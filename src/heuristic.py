import logging
import math


def manhattan_heuristic(puzzle, solution):
    """Sum of Manhattan distances of each tile to its final placement"""
    cost = 0
    for row in range(puzzle.size):
        for column in range(puzzle.size):
            digit = puzzle.currentState[row][column]
            if digit == 0:
                continue
            (expected_row, expected_column) = solution.positions[digit]

            x_distance = abs(row - expected_row)
            y_distance = abs(column - expected_column)

            cost += x_distance + y_distance
    return cost


def euclidean_heuristic(puzzle, solution):
    """Sum of Euclidean distances of each tile to its final placement"""
    cost = 0
    for row in range(puzzle.size):
        for column in range(puzzle.size):
            digit = puzzle.currentState[row][column]
            if digit == 0:
                continue
            (expected_row, expected_column) = solution.positions[digit]

            x_distance = row - expected_row
            y_distance = column - expected_column
            # √( (x1 -x2)² + (y1 - y2)² )
            cost += math.sqrt(x_distance ** 2 + y_distance ** 2)
    return cost


def hamming_heuristic(puzzle, solution):
    "return a cost equal to misplaced tiles."
    cost = 0
    for y in range(puzzle.size):
        for x in range(puzzle.size):
            if puzzle.currentState[y][x] == 0:
                continue
            digit = puzzle.currentState[y][x]
            if digit != solution.state[y][x]:
                cost += 1
    return cost
