import copy


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
    # data = [[j for j in i.split() if j != "|"] for i in data]
    print("data = {}".format(data))

    inputs = [i.split("|")[0].split() for i in data]

    solution = copy.deepcopy(inputs)

    for ix, entry in enumerate(inputs):
        print("entry = {}".format(entry))
        for sx, s in enumerate(entry):
            if len(s) == 2:
                str_1 = s
                solution[ix][sx] = 1
            if len(s) == 3:
                str_7 = s
                solution[ix][sx] = 7
            if len(s) == 4:
                str_4 = s
                solution[ix][sx] = 4
            if len(s) == 7:
                str_8 = s
                solution[ix][sx] = 8

        freqs = [sum([i in j for j in entry]) for i in "abcdef"]
        print("freqs = {}".format(freqs))
        # "f" solution is whatever character is missing from only one string

        # "a" solution is whatever's missing between 7 and 1 strings
        str_a = [i for i in str_7 if i not in str_1][0]
        print("str_a = {}".format(str_a))

        print("solution = {}".format(solution[ix]))


if __name__ == "__main__":
    part_1()
    part_2()