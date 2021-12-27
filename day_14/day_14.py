import itertools


def part_1():
    with open("input.txt") as f:
        data = f.read()

    template = data.split("\n\n")[0]
    rules = dict(l.split(" -> ") for l in data.split("\n\n")[1].splitlines())

    for _ in range(10):
        next_template = ""
        for i in range(len(template) - 1):
            pair = template[i] + template[i + 1]
            next_template += pair[0] + rules[pair] if pair in rules else pair[0]
        next_template += template[-1]
        template = next_template

    letter_counts = [template.count(s) for s in set(template)]
    print("part 1 answer = {}".format(max(letter_counts) - min(letter_counts)))


def part_2():
    with open("input.txt") as f:
        data = f.read()
    template = data.split("\n\n")[0]
    rules = dict(l.split(" -> ") for l in data.split("\n\n")[1].splitlines())

    # all the unique letters, assuming they can all be found in rules
    all_letters = "".join(set("".join(rules)))
    # all the unique pairs of letters
    all_pairs = itertools.product(all_letters, all_letters)

    # dict to keep track of how many of each letter is present
    letter_freqs = dict([(s, template.count(s)) for s in all_letters])
    # dict to keep track of how many of each pair is present
    pair_freqs = dict([(a + b, template.count(a + b)) for a, b in all_pairs])

    for _ in range(40):
        pair_freq_changes = dict(
            [(a + b, 0) for a, b in itertools.product(all_letters, all_letters)]
        )
        letter_freq_changes = dict([(s, 0) for s in all_letters])

        for pair, value in pair_freqs.items():
            if pair in rules:
                # split pair, remove them
                pair_freq_changes[pair] -= value
                # add new pairs from insertion of new letter
                pair_freq_changes[pair[0] + rules[pair]] += value
                pair_freq_changes[rules[pair] + pair[1]] += value
                letter_freq_changes[rules[pair]] += value

        for pair in pair_freqs:
            pair_freqs[pair] += pair_freq_changes[pair]
        for letter in letter_freqs:
            letter_freqs[letter] += letter_freq_changes[letter]

    part_2_answer = max(letter_freqs.values()) - min(letter_freqs.values())
    print("part 2 answer = {}".format(part_2_answer))


if __name__ == "__main__":
    part_1()
    part_2()