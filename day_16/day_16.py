from collections import deque
import numpy as np


def pop_multi(d, n):
    return [d.popleft() for _ in range(n)]


def bin_to_int(bin):
    return int("".join(str(i) for i in bin), 2)


def parse_literal(bin, versions):
    """
    Package is a literal value.

    Literal value packets encode a single binary number. To do this, the binary number is padded with leading zeroes until its length is a multiple of four bits, and then it is broken into groups of four bits. Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit. These groups of five bits immediately follow the packet header.
    """
    literal_bin = []
    end_literal = False
    while not end_literal:
        literal_group = pop_multi(bin, 5)
        # add bits to overall literal value
        literal_bin.extend(literal_group[1:])
        if literal_group[0] == 0:
            # means this is the last group
            end_literal = True

    # return value
    return bin_to_int(literal_bin)


def parse_operator(bin, versions):
    """
    Every other type of packet (any packet with a type ID other than 4) represent an operator that performs some calculation on one or more sub-packets contained within.

    An operator packet contains one or more packets. To indicate which subsequent binary data represents its sub-packets, an operator packet can use one of two modes indicated by the bit immediately after the packet header; this is called the length type ID:

    If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
    If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.

    Finally, after the length type ID bit and the 15-bit or 11-bit field, the sub-packets appear.
    """
    length_type_ID = pop_multi(bin, 1)[0]
    values = []
    if length_type_ID == 0:
        # next 15 bits represent total length of sub-packets
        len_packet = bin_to_int(pop_multi(bin, 15))
        bin_len_before = len(bin)
        bin_len_current = bin_len_before
        while bin_len_before - bin_len_current < len_packet:
            values.append(parse_packet(bin, versions))
            bin_len_current = len(bin)
    else:
        # next 11 bits represent number of sub-packets
        n_subpackets = bin_to_int(pop_multi(bin, 11))
        for _ in range(n_subpackets):
            values.append(parse_packet(bin, versions))

    return values


def parse_packet(bin, versions):
    # add this packet's version to our big list of version #s
    version = bin_to_int(pop_multi(bin, 3))
    versions.append(version)

    # parse type_ID for package type
    type_ID = bin_to_int(pop_multi(bin, 3))
    if type_ID == 4:
        # literal value
        value = parse_literal(bin, versions)
    else:
        # operator
        values = parse_operator(bin, versions)
        if type_ID == 0:
            # value equal to sum of sub-packet values
            value = sum(values)
        elif type_ID == 1:
            # value equal to product of sub-packet values
            value = np.product(values)
        elif type_ID == 2:
            # value equal to minimum of sub-packet values
            value = min(values)
        elif type_ID == 3:
            # value equal to maximum of sub-packet values
            value = max(values)
        elif type_ID == 5:
            # value equal to 1 if first sub-packet value > second else 0
            value = 1 if values[0] > values[1] else 0
        elif type_ID == 6:
            # value equal to 1 if first sub-packet value < second else 0
            value = 1 if values[0] < values[1] else 0
        elif type_ID == 7:
            # value equal to 1 if first sub-packet value == second else 0
            value = 1 if values[0] == values[1] else 0

    return value


def day_16():
    # read data
    with open("input.txt") as f:
        input = f.read()
    # convert to hex
    input_hexint = int(input, base=16)
    # convert to list of strs representing binary number
    input_bin = (bin(input_hexint))[2:].zfill(len(input) * 4)
    # convert to deque of ints representing binary number
    input_bin = deque([int(i) for i in input_bin])
    # tracks all subpackage versions
    versions = []
    # recursively parse input_bin, keeping track of version #s and values
    packet_value = parse_packet(input_bin, versions)

    part_1_answer = sum(versions)
    part_2_answer = packet_value

    print("part_1_answer = {}".format(part_1_answer))
    print("part_2_answer = {}".format(part_2_answer))


if __name__ == "__main__":
    day_16()