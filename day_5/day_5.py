import numpy as np


def add_to_ventmap(ventmap, coords):
    for coord in coords:
        ventmap[coord] += 1
    return ventmap


def part_1():
    with open("input.txt") as f:
        data = f.read().splitlines()

    # remove arrows
    data = [i.split("->") for i in data]
    # ints
    data = np.array([[[int(k) for k in j.split(",")] for j in i] for i in data])

    # entries representing horizontal lines
    horiz_lines = data[:, 0, 1] == data[:, 1, 1]
    # entries representing vertical lines
    verti_lines = data[:, 0, 0] == data[:, 1, 0]
    # entries representing horizontal or vertical lines
    valid_data = data[horiz_lines + verti_lines]

    ventmap = np.zeros(
        (np.max(valid_data[:, :, 0]) + 1, np.max(valid_data[:, :, 1]) + 1)
    )

    for entry in data[horiz_lines]:
        xmin = min(entry[0, 0], entry[1, 0])
        xmax = max(entry[0, 0], entry[1, 0])
        assert entry[0, 1] == entry[1, 1]
        y = entry[0, 1]

        xcoords = np.arange(xmin, xmax + 1)
        line_coords = zip(xcoords, np.full(len(xcoords), int(y)))
        ventmap = add_to_ventmap(ventmap, line_coords)

    for entry in data[verti_lines]:
        ymin = min(entry[0, 1], entry[1, 1])
        ymax = max(entry[0, 1], entry[1, 1])
        assert entry[0, 0] == entry[1, 0]
        x = entry[0, 0]

        ycoords = np.arange(ymin, ymax + 1)
        line_coords = zip(np.full(len(ycoords), int(x)), ycoords)
        ventmap = add_to_ventmap(ventmap, line_coords)

    n_overlaps = np.sum(ventmap > 1)
    print("part 1 answer = {}".format(n_overlaps))


def part_2():
    with open("input.txt") as f:
        data = f.read().splitlines()

    # remove arrows
    data = [i.split("->") for i in data]
    # ints
    data = np.array([[[int(k) for k in j.split(",")] for j in i] for i in data])

    # entries representing horizontal lines
    horiz_lines = data[:, 0, 1] == data[:, 1, 1]
    # entries representing vertical lines
    verti_lines = data[:, 0, 0] == data[:, 1, 0]
    # assume the rest are 45 degree diagonal
    diag_data = data[np.invert(horiz_lines + verti_lines)]

    ventmap = np.zeros((np.max(data[:, :, 0]) + 1, np.max(data[:, :, 1]) + 1))

    for entry in data[horiz_lines]:
        xmin = min(entry[0, 0], entry[1, 0])
        xmax = max(entry[0, 0], entry[1, 0])
        assert entry[0, 1] == entry[1, 1]
        y = entry[0, 1]

        xcoords = np.arange(xmin, xmax + 1)
        line_coords = zip(xcoords, np.full(len(xcoords), int(y)))
        ventmap = add_to_ventmap(ventmap, line_coords)

    for entry in data[verti_lines]:
        ymin = min(entry[0, 1], entry[1, 1])
        ymax = max(entry[0, 1], entry[1, 1])
        assert entry[0, 0] == entry[1, 0]
        x = entry[0, 0]

        ycoords = np.arange(ymin, ymax + 1)
        line_coords = zip(np.full(len(ycoords), int(x)), ycoords)
        ventmap = add_to_ventmap(ventmap, line_coords)

    for entry in diag_data:
        xa = entry[0, 0]
        xb = entry[1, 0]
        ya = entry[0, 1]
        yb = entry[1, 1]
        xmin = min(xa, xb)
        ymin = min(ya, yb)
        xmax = max(xa, xb)
        ymax = max(ya, yb)

        xcoords = np.arange(xmin, xmax + 1)
        if xa > xb:
            xcoords = xcoords[::-1]
        ycoords = np.arange(ymin, ymax + 1)
        if ya > yb:
            ycoords = ycoords[::-1]
        line_coords = zip(xcoords, ycoords)
        ventmap = add_to_ventmap(ventmap, line_coords)

    n_overlaps = np.sum(ventmap > 1)
    print("part 2 answer = {}".format(n_overlaps))


if __name__ == "__main__":
    part_1()
    part_2()