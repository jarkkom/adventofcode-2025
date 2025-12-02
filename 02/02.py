#! /usr/bin/env python3


def parse_input(input_data):
    ranges = []
    for line in input_data.splitlines():
        range_parts = line.split(",")
        for part in range_parts:
            if "-" not in part:
                continue

            start, end = part.split("-")
            ranges.append((int(start), int(end)))
    return ranges


def part1(input_data):
    id_ranges = parse_input(input_data)

    sum = 0

    for id_range in id_ranges:
        for i in range(id_range[0], id_range[1] + 1):
            s = str(i)
            if len(s) % 2 != 0:
                continue

            half = len(s) // 2
            if s[:half] == s[half:]:
                sum += i

    return sum


if __name__ == "__main__":
    with open("02/sample.txt") as f:
        input_data = f.read()
        print(f"Part1 sample: {part1(input_data)}")

    with open("02/input.txt") as f:
        input_data = f.read()
        print(f"Part1 input: {part1(input_data)}")
