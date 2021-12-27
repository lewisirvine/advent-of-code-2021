import numpy as np


def flash_neighbours(coord, energies):
    """
    Given a coordinate and an array of energies, increase all of that coordinate's neighbours' energies by 1. Checks for boundaries and coordinates that have already flashed this turn (=0).
    """
    flash_increases = np.zeros(np.shape(energies))
    for delta in [
        [-1, -1],
        [-1, 1],
        [-1, 0],
        [1, -1],
        [1, 1],
        [1, 0],
        [0, -1],
        [0, 1],
    ]:
        flash_coord = coord + delta
        if (
            all(flash_coord >= 0)
            and all(flash_coord < np.shape(energies))
            and energies[tuple(flash_coord)] != 0
        ):
            flash_increases[tuple(flash_coord)] += 1
    energies += flash_increases
    return energies


def part_1():
    with open("input.txt") as f:
        energies = f.read().splitlines()
    energies = np.array([[int(s) for s in l] for l in energies])

    total_flashes = 0
    for _ in range(100):
        # increase all energies by 1
        energies += 1

        # find fish that flash, increase neighbours' energies and iterate
        n_flashes = np.nan  # passes first while condition
        while n_flashes:
            # any fish with energy > 9 will flash, get map + coordinates
            flash_map = energies > 9
            flash_coords = np.argwhere(flash_map)

            # number of fish that will flash this round
            n_flashes = len(flash_coords)
            total_flashes += n_flashes

            # for every fish that flashes, find all eight neighbours and increase their energies by 1
            for coord in flash_coords:
                energies = flash_neighbours(coord, energies)

            # all fish that flashed get reset to 0
            energies[flash_map] = 0

    print("part 1 answer = {}".format(total_flashes))


def part_2():
    with open("input.txt") as f:
        energies = f.read().splitlines()
    energies = np.array([[int(s) for s in l] for l in energies])

    for i in range(1000):
        # increase all energies by 1
        energies += 1

        # find fish that flash, increase neighbours' energies and iterate
        n_flashes = np.nan  # passes first while condition
        while n_flashes:
            # any fish with energy > 9 will flash, get map + coordinates
            flash_map = energies > 9
            flash_coords = np.argwhere(flash_map)

            # number of fish that will flash this round
            n_flashes = len(flash_coords)

            # for every fish that flashes, find all eight neighbours and increase their energies by 1
            for coord in flash_coords:
                energies = flash_neighbours(coord, energies)

            # all fish that flashed get reset to 0
            energies[flash_map] = 0

        if (energies == 0).all():
            print("SYNC")
            print("part 2 answer = {}".format(i + 1))
            return


if __name__ == "__main__":
    part_1()
    part_2()