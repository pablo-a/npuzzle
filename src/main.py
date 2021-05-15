from parsing.parser import parse_stdin
from solver import Astar
import argparse
import logging
import cProfile


def main():

    if args.loglevel != "NONE":
        logging.basicConfig(level=args.loglevel)

    initial_puzzle = parse_stdin()

    solver = Astar(initial_puzzle)
    solver.set_search_type(args.searchtype)
    solver.set_heuristic(args.heuristic)
    if solver.is_solvable():
        solver.solve()
    else:
        print("This puzzle is not solvable !")


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-l",
        "--loglevel",
        type=str,
        default="ERROR",
        choices=["NONE", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Setup the log level.",
    )

    parser.add_argument(
        "-s",
        "--searchtype",
        type=str,
        default="A*",
        choices=["A*", "uniform", "greedy"],
        help="Choose a type of search algorithm.",
    )

    parser.add_argument(
        "-H",
        "--heuristic",
        type=str,
        default="hamming",
        choices=["manhattan", "hamming", "euclidean"],
        help="Choose an heuristic to solve puzzle.",
    )

    parser.add_argument(
        "-P",
        "--profiling",
        action="store_true",
        help="Activate Profiling",
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    # if we want some profiling
    if args.profiling:
        cProfile.run("main()")
    else:
        main()
