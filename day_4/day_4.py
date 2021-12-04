import numpy as np


def part_1():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    calls = np.array([int(i) for i in data[0].split(",")])
    print("calls = {}".format(calls))
    grids = np.array([[int(i) for i in j.split(" ") if i] for j in data[2:] if j])

    gridsize = 5
    n_grids = np.product(np.shape(grids)) / (gridsize ** 2)

    grids = grids.reshape((n_grids, gridsize, gridsize))
    print("grids = {}".format(grids))

    call_grids = np.zeros(np.shape(grids))
    has_won = False  # has someone won yet?
    for call in calls:
        # find matching numbers
        call_grids += grids == call
        # print("call_grids = {}".format(call_grids))

        # check for winning rows / columns
        for gx, call_grid in enumerate(call_grids):
            for row in call_grid:
                if sum(row) == 5:
                    has_won = True
            for column in call_grid.T:
                if sum(column) == 5:
                    has_won = True
            if has_won:
                winning_grid = gx
                break

        if has_won:
            winning_number = call
            break

    print("winning_grid = {}".format(winning_grid))
    print("winning_number = {}".format(winning_number))

    winning_unmarked_numbers = grids[gx][call_grids[gx] == False]

    part_1_answer = sum(winning_unmarked_numbers) * winning_number

    print("part_1_answer = {}".format(part_1_answer))


def part_2():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    calls = np.array([int(i) for i in data[0].split(",")])
    print("calls = {}".format(calls))
    grids = np.array([[int(i) for i in j.split(" ") if i] for j in data[2:] if j])

    gridsize = 5
    n_grids = np.product(np.shape(grids)) / (gridsize ** 2)

    grids = grids.reshape((n_grids, gridsize, gridsize))
    print("grids = {}".format(grids))

    call_grids = np.zeros(np.shape(grids))
    winning_grids = np.zeros(n_grids)
    losing_grid = None
    found_loser = False
    loser_has_won = False
    for call in calls:
        # find matching numbers
        call_grids += grids == call

        # check for winning rows / columns
        for gx, call_grid in enumerate(call_grids):
            for row in call_grid:
                if sum(row) == 5:
                    winning_grids[gx] = 1
            for column in call_grid.T:
                if sum(column) == 5:
                    winning_grids[gx] = 1

            print("sum(winning_grids) = {}".format(sum(winning_grids)))
            if sum(winning_grids) == n_grids - 1 and not found_loser:
                losing_grid = np.where(winning_grids == 0)[0]
                found_loser = True
            elif sum(winning_grids) == n_grids:
                loser_has_won = True
                last_number = call
                break

        if loser_has_won:
            break

    print("losing_grid = {}".format(losing_grid))
    print("last_number = {}".format(last_number))

    losing_unmarkerd_numbers = grids[gx][call_grids[gx] == False]

    part_2_answer = sum(losing_unmarkerd_numbers) * last_number

    print("part_2_answer = {}".format(part_2_answer))


if __name__ == "__main__":
    part_1()
    part_2()
