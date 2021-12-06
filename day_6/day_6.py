import numpy as np


def part_1():
    with open("input.txt") as f:
        data = f.read().splitlines()[0]
    fishes = [int(i) for i in data.split(",")]

    n_days = 80
    for _ in range(n_days):
        for f in range(len(fishes)):
            if fishes[f] == 0:
                fishes.append(8)
                fishes[f] = 6
            else:
                fishes[f] -= 1

    print("part 1 answer = {}".format(len(fishes)))


def part_2():
    with open("input.txt") as f:
        data = f.read().splitlines()[0]
    fishes = np.array([int(i) for i in data.split(",")])

    n_numbers = 9
    # fish tracker contains how many fish have n days remaining
    fish_tracker = np.zeros(n_numbers)
    for n in range(n_numbers):
        fish_tracker[n] = np.sum(fishes == n)

    n_days = 256
    for _ in range(n_days):
        # number of fish with 0 days
        n_zeros = fish_tracker[0]
        # reduce days for all fish by 1
        for n in range(n_numbers - 1):
            fish_tracker[n] = fish_tracker[n + 1]
        # fish at 0 go to 6
        fish_tracker[6] += n_zeros
        # spawn new fish at 8
        fish_tracker[8] = n_zeros

    print("part 2 answer = {}".format(int(sum(fish_tracker))))


if __name__ == "__main__":
    part_1()
    part_2()