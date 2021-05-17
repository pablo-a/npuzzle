# N-Puzzle

[![CI status](https://github.com/pablo-a/npuzzle/actions/workflows/python-app.yml/badge.svg)](https://github.com/pablo-a/npuzzle/actions/workflows/python-app.yml)

## What is this project ?

This project written in Python aims to solve N-puzzle games using the A\* search algorithm or one of its variants.

## How to use ?

### Pre requisites

- Python 3.6

### Usage

We just need to generate a puzzle and pass it to our solver :

- Generator Usage : `python gen.py [-h] [-s] [-u] [-i ITERATIONS] size `

  - `-h` : Help
  - `-s` : Puzzle must be **solvable**
  - `-u` : Puzzle must be **unsolvable**
  - `-i` : How many iterations needed to shuffle puzle
  - `<size>` : Puzzle size

- Solver Usage : `python src/main.py [-h] [-l {NONE,DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-s {A*,uniform,greedy}] [-H {manhattan,hamming,euclidean}]`
  - `-h` : Help
  - `-l` : Log Level (default to `ERROR`)
  - `-s` : Solver **strategy** to use (default to `A*`)
  - `-H` : Solver **heuristic** to use (default to `hamming`)
  - `-P` : Use Profiling

For example : `python gen.py 3 -s | python src/main.py`

## Explainations on Algorithms to solve this problem

To solve this problem we can use different strategies (or algorithms), each one having its pros and cons.

Those strategies make also use of **heuristics** that allow them to measure how much a _move_ (here it means change one tile's place) is relevant or not by giving it a score.

We generate all the possible **moves** from an initial position and then use a **priority queue** to save them. We then always try the solutions that seems on top of this queue : the ones with the highest score given by the choosen **heuristic**

### Strategies

- **`A*`** : quite efficient and quite optimal solution.
- **`uniform`** : low efficiency but optimal solution.
- **`greedy`** : very efficient but sub-optimal solution.

### Heuristics

- **`manhattan`**
- **`hamming`**
- **`euclidean`**

# Interesting resources

This [Blog](https://www.redblobgames.com/pathfinding/a-star/introduction.html) is just amazing to understand algorithms, heuristics by visualizing them.
