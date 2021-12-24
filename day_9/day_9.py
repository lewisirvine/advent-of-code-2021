import numpy as np


def part_1():
    with open("input.txt") as f:
        data = f.read().splitlines()
    data = [[int(i) for i in s] for s in data]

    part_1_solution = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            this_depth = data[i][j]
            left_check = this_depth < data[i - 1][j] if i != 0 else True
            right_check = this_depth < data[i + 1][j] if i != len(data) - 1 else True
            up_check = this_depth < data[i][j - 1] if j != 0 else True
            down_check = this_depth < data[i][j + 1] if j != len(data[0]) - 1 else True

            if sum([left_check, right_check, up_check, down_check]) == 4:
                part_1_solution += this_depth + 1

    print("part_1_solution = {}".format(part_1_solution))


def find_basin_size(low_point, data):
    basin_points = [low_point]
    for _ in range(100):
        for point in basin_points:
            surrounding_points = [
                (point[0] - 1, point[1]),
                (point[0] + 1, point[1]),
                (point[0], point[1] - 1),
                (point[0], point[1] + 1),
            ]
            for surr_point in surrounding_points:
                if (
                    surr_point not in basin_points
                    and surr_point[0] >= 0
                    and surr_point[0] < len(data)
                    and surr_point[1] >= 0
                    and surr_point[1] < len(data[0])
                    and data[surr_point] < 9
                ):
                    basin_points.append(surr_point)
    return len(basin_points)


def part_2():
    with open("input.txt") as f:
        data = f.read().splitlines()
    data = np.array([[int(i) for i in s] for s in data])

    low_points = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            this_depth = data[i][j]
            left_check = this_depth < data[i - 1][j] if i != 0 else True
            right_check = this_depth < data[i + 1][j] if i != len(data) - 1 else True
            up_check = this_depth < data[i][j - 1] if j != 0 else True
            down_check = this_depth < data[i][j + 1] if j != len(data[0]) - 1 else True
            if sum([left_check, right_check, up_check, down_check]) == 4:
                low_points.append((i, j))

    basin_sizes = [find_basin_size(low_point, data) for low_point in low_points]
    bsize_ordered = sorted(basin_sizes, reverse=True)
    part_2_solution = bsize_ordered[0] * bsize_ordered[1] * bsize_ordered[2]

    print("part_2_solution = {}".format(part_2_solution))


if __name__ == "__main__":
    part_1()
    part_2()