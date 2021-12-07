from operator import pos
import numpy as np


def part_1():
    positions = np.loadtxt("input.txt", delimiter=",").astype("int")
    solutions = np.zeros(max(positions))
    for s in range(max(positions)):
        solutions[s] = sum(np.abs(positions - s))

    min_solution = np.argmin(solutions)
    print("part 1 answer = {}".format(solutions[min_solution]))


def part_2():
    positions = np.loadtxt("input.txt", delimiter=",").astype("int")
    solutions = np.zeros(max(positions))
    for s in range(max(positions)):
        distances_to_solution = np.abs(positions - s)
        solutions[s] = sum(sum(range(d + 1)) for d in distances_to_solution)

    min_solution = np.argmin(solutions)
    print("part 2 answer = {}".format(solutions[min_solution]))


if __name__ == "__main__":
    part_1()
    part_2()