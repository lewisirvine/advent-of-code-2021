import numpy as np


def part_1():
    with open("input.txt") as f:
        data = f.read().splitlines()
    outputs = [i.split("|")[1].split() for i in data]

    unique_lens = [2, 3, 4, 7]
    n_unique_lens = 0

    for entry in outputs:
        for s in entry:
            if len(s) in unique_lens:
                n_unique_lens += 1

    print("part 1 answer = {}".format(n_unique_lens))


def part_2():
    with open("input.txt") as f:
        data = f.read().splitlines()
    inputs = [i.split("|")[0].split() for i in data]
    outputs = [i.split("|")[1].split() for i in data]

    part_2_solution = []

    for ix, entry in enumerate(inputs):
        solutions = [""] * 10

        # "f" solution is whatever character is missing from only one string
        freqs = [sum(i in j for j in entry) for i in "abcdefg"]
        str_f = "abcdefg"[np.argmax(freqs)]

        # special numbers with unique number of segs
        for s in entry:
            # 1 has two segs
            if len(s) == 2:
                solutions[1] = s
            # 7 has three segs
            if len(s) == 3:
                solutions[7] = s
            # 4 has four segs
            if len(s) == 4:
                solutions[4] = s
            # 8 has all seven segs
            if len(s) == 7:
                solutions[8] = s

        # deduce the others
        for s in entry:
            if len(s) == 5:
                # 2 has five segs and no f seg
                if str_f not in s:
                    solutions[2] = s
                # 3 has five segs and all the segs in 1
                elif all(i in s for i in solutions[1]):
                    solutions[3] = s
                # 5 is the other five seg number
                else:
                    solutions[5] = s
            if len(s) == 6:
                # 9 has six segs and all the segs in 4
                if all(i in s for i in solutions[4]):
                    solutions[9] = s
                # 0 has six segs and all the segs in 7 (and isn't 9)
                elif all(i in s for i in solutions[7]):
                    solutions[0] = s
                # 6 is the other six seg number
                else:
                    solutions[6] = s

        # now solve output
        solution = ""
        for output in outputs[ix]:
            # how many shared segs?
            overlaps = [sum(s in i for s in output) for i in solutions]
            # is number of shared segs equal to len of output *and* solution?
            matches = [
                overlaps[i] == len(output) and len(output) == len(solutions[i])
                for i in range(len(solutions))
            ]
            # add the only index that is True
            solution += str(np.argmax(matches))
        part_2_solution.append(int(solution))

    print("part 2 answer = {}".format(sum(part_2_solution)))


if __name__ == "__main__":
    part_1()
    part_2()