import numpy as np


def main():
    infile = "input.txt"

    with open(infile, "r") as f:
        commands = f.read().splitlines()
    commands = [c.split() for c in commands]

    depth = 0
    horiz = 0
    aim = 0

    for command in commands:
        direction = command[0]
        distance = int(command[1])

        if direction == "forward":
            horiz += distance
            depth += aim * distance
        elif direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance

    answer = depth * horiz
    print(answer)


if __name__ == "__main__":
    main()