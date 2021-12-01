import numpy as np


def main():
    infile = "input.txt"
    depths = np.loadtxt(infile)

    sliding_depths = []

    for dx in range(len(depths)):
        if dx < len(depths) - 2:
            sliding_depths.append(depths[dx] + depths[dx + 1] + depths[dx + 2])

    n_increases = sum(
        dx > 0 and sliding_depths[dx] > sliding_depths[dx - 1]
        for dx in range(len(sliding_depths))
    )
    print(n_increases)


if __name__ == "__main__":
    main()