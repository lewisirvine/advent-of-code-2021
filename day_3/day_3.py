import numpy as np


def binary_to_decimal(binary_number):
    len_number = len(binary_number)
    powers_of_2_rev = [2 ** i for i in range(len_number)][::-1]
    return sum(binary_number[i] * powers_of_2_rev[i] for i in range(len_number))


def part_1():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    n_entries = len(data)
    n_columns = len(data[0])

    gamma = []
    epsilon = []

    for column in range(n_columns):
        col_digits = [int(d[column]) for d in data]
        sum_col = sum(col_digits)
        if sum_col > n_entries / 2:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)

    gamma_decimal = binary_to_decimal(gamma)
    epsilon_decimal = binary_to_decimal(epsilon)

    part_1_answer = gamma_decimal * epsilon_decimal
    print("part_1_answer = {}".format(part_1_answer))


def part_2():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    data = np.array(
        [[int(data[i][j]) for j in range(len(data[i]))] for i in range(len(data))]
    )
    n_columns = len(data[0])

    # Oxygen
    oxy_data = data
    for column in range(n_columns):
        col_digits = oxy_data[:, column]
        sum_col = sum(col_digits)
        if sum_col >= len(oxy_data) / 2.0:
            # 1 more common, or equal
            oxy_data = oxy_data[oxy_data[:, column] == 1]
        else:
            # 0 more common
            oxy_data = oxy_data[oxy_data[:, column] == 0]
        if len(oxy_data) == 1:
            break

    oxygen_bin = oxy_data[0]
    oxygen_dec = binary_to_decimal(oxygen_bin)

    # CO2
    co2_data = data
    for column in range(n_columns):
        col_digits = co2_data[:, column]
        sum_col = sum(col_digits)
        if sum_col >= len(co2_data) / 2.0:
            # 1 more common, or equal
            co2_data = co2_data[co2_data[:, column] == 0]
        else:
            # 0 more common
            co2_data = co2_data[co2_data[:, column] == 1]
        if len(co2_data) == 1:
            break

    co2_bin = co2_data[0]
    co2_dec = binary_to_decimal(co2_bin)

    part_2_answer = oxygen_dec * co2_dec
    print("part_2_answer = {}".format(part_2_answer))


if __name__ == "__main__":
    part_1()
    part_2()