import numpy as np
from copy import deepcopy
import pdb


class Path:
    def __init__(self, points, end_id, connections, occupancies):
        self.points = points
        self.end_id = end_id
        self.connections = connections
        self.occupancies = occupancies

    def check_if_complete(self):
        # if last point corresponds to "end" index, return True
        return self.points[-1] == self.end_id

    def get_neighbours(self):
        # search connections for neighbours
        all_neighbours = np.argwhere(self.connections[self.points[-1]] > 0)[:, 0]
        # search occupancies for neighbours that can still be returned to
        valid_neighbours = [n for n in all_neighbours if self.occupancies[n] > 0]
        return valid_neighbours

    def generate_neighbour_paths(self):
        # find neighbours that can still be returned to
        neighbours = self.get_neighbours()
        # make some paths with each new neighbour on the end
        new_points = [self.points + [n] for n in neighbours]
        # create new occupancy list, taking 1 away from current endpoint to show we've been there
        new_occupancies = deepcopy(self.occupancies)
        new_occupancies[self.points[-1]] -= 1
        # create new Path objects for each valid neighbour
        new_paths = [
            Path(
                points,
                self.end_id,
                self.connections,
                new_occupancies,
            )
            for points in new_points
        ]
        return new_paths


def part_1():
    with open("input.txt") as f:
        data = f.read().splitlines()
    print("data = {}".format(data))

    # find all unique places and assign each a unique index, found in point_dict
    all_points = [l.split("-") for l in data]
    unique_points = {item for sublist in all_points for item in sublist}
    point_dict = {name: i for i, name in enumerate(unique_points)}
    print("point_dict = {}".format(point_dict))

    # build a map of connections: 1 = connected, 0 = not connected
    connections = np.zeros((len(unique_points), len(unique_points)))
    for line in data:
        start, end = line.split("-")
        connections[point_dict[start], point_dict[end]] = 1
        connections[point_dict[end], point_dict[start]] = 1
    print(connections)

    # occupancies tracks how many visits there are left until that point is invalid. If point name is lowercase, we can visit there one time. Otherwise we can visit an unlimited number of times
    uppers = [s.isupper() for s in unique_points]
    occupancies = np.where(uppers, np.inf, 1)

    start_id = point_dict["start"]
    end_id = point_dict["end"]

    # start a list of Path objects that will get added to
    paths = [Path([start_id], end_id, connections, occupancies)]
    # a (blank) list of valid paths to the end
    valid_paths = []
    for p in paths:
        # if path finishes at "end", add to valid paths
        if p.check_if_complete():
            valid_paths.append(p)
        # if not, search for neighbours and add corresponding Path objects to path list.
        else:
            paths.extend(p.generate_neighbour_paths())

    for p in valid_paths:
        print(p.points)
    print("part 1 answer = {}".format(len(valid_paths)))


class Path2:
    def __init__(
        self, points, end_id, connections, occupancies, original_occupancies, used_bonus
    ):
        self.points = points
        self.end_id = end_id
        self.connections = connections
        self.original_occupancies = original_occupancies
        self.occupancies = occupancies
        self.used_bonus = used_bonus

    def check_if_complete(self):
        # if last point corresponds to "end" index, return True
        return self.points[-1] == self.end_id

    def get_neighbours(self):
        # search connections for neighbours
        all_neighbours = np.argwhere(self.connections[self.points[-1]] > 0)[:, 0]
        # search occupancies for neighbours that can still be returned to
        valid_neighbours = [n for n in all_neighbours if self.occupancies[n] > 0]
        return valid_neighbours

    def generate_neighbour_paths(self):
        # print("")

        # find neighbours that can still be returned to
        neighbours = self.get_neighbours()
        # make some paths with each new neighbour on the end
        new_points = [self.points + [n] for n in neighbours]

        # create new occupancy list, taking 1 away from current endpoint to show we've been there
        new_occupancies = deepcopy(self.occupancies)

        # small cave condition
        if (
            self.original_occupancies[self.points[-1]] == 2
            and new_occupancies[self.points[-1]] == 1
            and not self.used_bonus
        ):
            new_occupancies[self.original_occupancies == 2] -= 1
            new_used_bonus = True
        else:
            new_occupancies[self.points[-1]] -= 1
            new_used_bonus = self.used_bonus

        # create new Path objects for each valid neighbour
        new_paths = [
            Path2(
                points,
                self.end_id,
                self.connections,
                new_occupancies,
                self.original_occupancies,
                new_used_bonus,
            )
            for points in new_points
        ]
        return new_paths


def part_2():
    with open("input.txt") as f:
        data = f.read().splitlines()
    print("data = {}".format(data))

    # find all unique places and assign each a unique index, found in point_dict
    all_points = [l.split("-") for l in data]
    unique_points = {item for sublist in all_points for item in sublist}
    point_dict = {name: i for i, name in enumerate(unique_points)}
    print("point_dict = {}".format(point_dict))

    # build a map of connections: 1 = connected, 0 = not connected
    connections = np.zeros((len(unique_points), len(unique_points)))
    for line in data:
        start, end = line.split("-")
        connections[point_dict[start], point_dict[end]] = 1
        connections[point_dict[end], point_dict[start]] = 1
    print(connections)

    # occupancies tracks how many visits there are left until that point is invalid. If point name is lowercase, we can visit there one time. Otherwise we can visit an unlimited number of times
    uppers = [s.isupper() for s in unique_points]
    start_ends = [s in ["start", "end"] for s in unique_points]
    occupancies = np.where(uppers, np.inf, np.where(start_ends, 1, 2))
    print("occupancies = {}".format(occupancies))

    start_id = point_dict["start"]
    end_id = point_dict["end"]

    # start a list of Path objects that will get added to
    paths = [Path2([start_id], end_id, connections, occupancies, occupancies, False)]
    # a (blank) list of valid paths to the end
    valid_paths = []
    for p in paths:
        # if path finishes at "end", add to valid paths
        if p.check_if_complete():
            valid_paths.append(p)
        # if not, search for neighbours and add corresponding Path objects to path list.
        else:
            paths.extend(p.generate_neighbour_paths())

    # something went wrong, so get rid of any solutions with -1 in their occupancies
    print(
        "part 2 answer = {}".format(
            len([p for p in valid_paths if -1 not in p.occupancies])
        )
    )


if __name__ == "__main__":
    # part_1()
    part_2()
