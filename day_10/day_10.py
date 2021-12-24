def check_closers(closer, expected_closers):
    if expected_closers[0] != closer:
        return closer
    expected_closers.pop(0)
    return None


def part_1():
    with open("input.txt") as f:
        data = f.read().splitlines()

    error_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    part_1_answer = 0

    for line in data:
        expected_closers = []
        corrupted_line = False
        for s in line:
            if not corrupted_line:
                error = None
                if s == "(":
                    expected_closers.insert(0, ")")
                elif s == "[":
                    expected_closers.insert(0, "]")
                elif s == "{":
                    expected_closers.insert(0, "}")
                elif s == "<":
                    expected_closers.insert(0, ">")
                elif s in [")", "]", "}", ">"]:
                    error = check_closers(s, expected_closers)
                if error:
                    part_1_answer += error_scores[error]
                    corrupted_line = True

    print("part_1_answer = {}".format(part_1_answer))


def part_2():
    with open("input.txt") as f:
        data = f.read().splitlines()

    corrupted_idxs = []
    for lx, line in enumerate(data):
        expected_closers = []
        for s in line:
            if lx not in corrupted_idxs:
                error = None
                if s == "(":
                    expected_closers.insert(0, ")")
                elif s == "[":
                    expected_closers.insert(0, "]")
                elif s == "{":
                    expected_closers.insert(0, "}")
                elif s == "<":
                    expected_closers.insert(0, ">")
                elif s in [")", "]", "}", ">"]:
                    error = check_closers(s, expected_closers)
                if error:
                    corrupted_idxs.append(lx)

    uncorrupted_lines = [l for lx, l in enumerate(data) if lx not in corrupted_idxs]

    all_closers = []
    for line in uncorrupted_lines:
        expected_closers = []
        for s in line:
            error = None
            if s == "(":
                expected_closers.insert(0, ")")
            elif s == "[":
                expected_closers.insert(0, "]")
            elif s == "{":
                expected_closers.insert(0, "}")
            elif s == "<":
                expected_closers.insert(0, ">")
            elif s in [")", "]", "}", ">"]:
                error = check_closers(s, expected_closers)
        all_closers.append(expected_closers)

    closer_points = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []
    for line in all_closers:
        score = 0
        for s in line:
            score = score * 5 + closer_points[s]
        scores.append(score)

    part_2_solution = sorted(scores)[(len(scores) - 1) / 2]
    print("part_2_solution = {}".format(part_2_solution))


if __name__ == "__main__":
    part_1()
    part_2()