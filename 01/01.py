#! /usr/bin/env python3


def part1(input_data):
    position = 50

    zeros = 0

    for line in input_data.splitlines():
        direction = line[0]
        value = line[1:]
        value = int(value)

        if direction == "R":
            position += value
        elif direction == "L":
            position -= value

        position %= 100

        if position == 0:
            zeros += 1

    return zeros


def part2(input_data):
    position = 50

    zeros = 0

    for line in input_data.splitlines():
        direction = line[0]
        value = line[1:]
        value = int(value)

        step = 0
        if direction == "R":
            step = 1
        elif direction == "L":
            step = -1

        while value > 0:
            position += step
            position %= 100
            if position == 0:
                zeros += 1

            value -= 1

    return zeros


if __name__ == "__main__":
    with open("01/sample.txt") as f:
        input_data = f.read()
        p1_zeros = part1(input_data)
        print(f"Part1 sample: {p1_zeros}")
        assert p1_zeros == 3

        p2_zeros = part2(input_data)
        print(f"Part2 sample: {p2_zeros}")
        assert p2_zeros == 6

    with open("01/input.txt") as f:
        input_data = f.read()
        p1_zeros = part1(input_data)
        print(f"Part1 input: {p1_zeros}")
        assert p1_zeros == 1100

        p2_zeros = part2(input_data)
        print(f"Part2 input: {p2_zeros}")
        assert p2_zeros == 6358
