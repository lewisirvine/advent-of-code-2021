import numpy as np


def part_1():
    with open("input.txt") as f:
        data = f.read()
    dot_coords = np.array(
        [[int(i) for i in l.split(",")] for l in data.split("\n\n")[0].splitlines()]
    )
    instructions = data.split("\n\n")[1].splitlines()
    instructions = [i.lstrip("fold along").split("=") for i in instructions]

    grid = np.zeros((max(dot_coords[:, 0]) + 2, max(dot_coords[:, 1]) + 2))
    gridshape = np.shape(grid)

    for coord in dot_coords:
        grid[coord[0], coord[1]] = 1

    for instruction in instructions[:1]:
        instruction[1] = int(instruction[1])
        assert instruction[1] in np.array(gridshape) / 2
        if instruction[0] == "y":
            assert all(grid[:, instruction[1]] == 0)
            for col in range(instruction[1]):
                grid[:, col] += grid[:, gridshape[1] - 1 - col]
            grid = grid[:, : instruction[1]]
        elif instruction[0] == "x":
            assert all(grid[instruction[1]] == 0)
            for row in range(instruction[1]):
                grid[row] += grid[gridshape[0] - 1 - row]
            grid = grid[: instruction[1]]
        gridshape = np.shape(grid)

    print("part 1 solution = {}".format(np.sum(grid > 0)))


def part_2():
    with open("input.txt") as f:
        data = f.read()
    dot_coords = np.array(
        [[int(i) for i in l.split(",")] for l in data.split("\n\n")[0].splitlines()]
    )
    instructions = data.split("\n\n")[1].splitlines()
    instructions = [i.lstrip("fold along").split("=") for i in instructions]

    grid = np.zeros((max(dot_coords[:, 0]) + 2, max(dot_coords[:, 1]) + 2))
    gridshape = np.shape(grid)

    for coord in dot_coords:
        grid[coord[0], coord[1]] = 1

    for instruction in instructions[:]:
        instruction[1] = int(instruction[1])

        assert instruction[1] in np.array(gridshape) / 2
        if instruction[0] == "y":
            assert all(grid[:, instruction[1]] == 0)
            for col in range(instruction[1]):
                grid[:, col] += grid[:, gridshape[1] - 1 - col]
            grid = grid[:, : instruction[1]]
        elif instruction[0] == "x":
            assert all(grid[instruction[1]] == 0)
            for row in range(instruction[1]):
                grid[row] += grid[gridshape[0] - 1 - row]
            grid = grid[: instruction[1]]
        gridshape = np.shape(grid)

    for j in range(gridshape[1]):
        line = ""
        for i in range(gridshape[0]):
            if grid[i, j] > 0:
                line += "#"
            else:
                line += "."
        print(line)


if __name__ == "__main__":
    part_1()
    part_2()