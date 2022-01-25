def fire(initial_velocity, xrange, yrange):
    positions = [[0, 0]]
    velocities = [initial_velocity]

    for step in range(1000):
        old_position = positions[step]
        old_velocity = velocities[step]
        new_position = [
            old_position[0] + old_velocity[0],
            old_position[1] + old_velocity[1],
        ]
        new_velocity = [
            max(0, old_velocity[0] - 1),
            old_velocity[1] - 1,
        ]
        positions.append(new_position)
        velocities.append(new_velocity)

        # check if in target
        if (
            new_position[0] >= xrange[0]
            and new_position[0] <= xrange[1]
            and new_position[1] >= yrange[0]
            and new_position[1] <= yrange[1]
        ):
            print(
                "\nHIT! vel = {}, {}".format(initial_velocity[0], initial_velocity[1])
            )
            max_height = max(p[1] for p in positions)
            print("max_height = {}".format(max_height))
            return max_height
    return -1


def day_17():
    with open("input.txt") as f:
        input = f.read()
    input = input.replace(",", "")
    input = input.replace("..", " ")
    input = input.replace("target area: x=", "")
    input = input.replace("y=", "")
    input = [int(i) for i in input.split(" ")]
    xrange = [min([input[0], input[1]]), max([input[0], input[1]])]
    yrange = [min([input[2], input[3]]), max([input[2], input[3]])]
    print("xrange = {}".format(xrange))
    print("yrange = {}".format(yrange))

    # x velocity can't be negative, and can't bypass target within first step
    xvels = range(xrange[1] + 1)
    yvels = range(-1000, 1000)

    highest_y = 0
    n_solutions = 0

    for y_vel in yvels:
        for x_vel in xvels:
            max_height = fire([x_vel, y_vel], xrange, yrange)
            if max_height >= 0:
                n_solutions += 1
                print("n_solutions = {}".format(n_solutions))
                if max_height > highest_y:
                    highest_y = max_height

    print("\n\nEND")
    print("highest_y = {}".format(highest_y))
    print("n_solutions = {}".format(n_solutions))


if __name__ == "__main__":
    day_17()