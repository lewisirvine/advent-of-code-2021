import numpy as np


def main():
    infile = "input.txt"
    depths = np.loadtxt(infile)

    n_increases = sum(
        dx > 0 and depths[dx] > depths[dx - 1] for dx in range(len(depths))
    )

    print(n_increases)


if __name__ == "__main__":
    main()