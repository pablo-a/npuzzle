import parsing.integrity as integrity
from data_model import ParsingError, PuzzleState
import pytest


def test_check_puzzle_unicity():
    integrity.check_puzzle_unicity([1, 2, 3, 4, 5, 6, 7, 8, 0])
    integrity.check_puzzle_unicity(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    )
    with pytest.raises(ParsingError):
        integrity.check_puzzle_unicity([1, 2, 3, 4, 5, 6, 7, 8, 8])
        integrity.check_puzzle_unicity([1, 1, 3, 4, 5, 6, 7, 8, 0])
        integrity.check_puzzle_unicity([12, 1, 3, 4, 5, 6, 7, 8, 12])


def test_check_correct_numbers():
    integrity.check_correct_numbers(3, [1, 2, 3, 4, 5, 6, 7, 8, 0])
    integrity.check_correct_numbers(
        4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    )
    with pytest.raises(ParsingError):
        integrity.check_correct_numbers(3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        integrity.check_correct_numbers(3, [1, 2, 3, 42])
        integrity.check_correct_numbers(4, [1, 2, 3, 56])
        integrity.check_correct_numbers(3, [1, 2, 3, 11, 17])


def test_check_numbers_present():
    integrity.check_numbers_present(3, [_ for _ in range(9)])
    integrity.check_numbers_present(4, [_ for _ in range(16)])
    integrity.check_numbers_present(5, [_ for _ in range(25)])
    with pytest.raises(ParsingError):
        integrity.check_numbers_present(3, [_ for _ in range(5)])
        integrity.check_numbers_present(3, [_ for _ in range(10)])
        integrity.check_numbers_present(4, [_ for _ in range(20)])
