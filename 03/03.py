#!/usr/bin/env python3


def parse_input(input_data):
    lines = input_data.splitlines()
    return [list(map(int, list(line))) for line in lines]


def part1(input_data):
    banks = parse_input(input_data)

    sum = 0

    for bank in banks:
        num = 0
        d1 = 0
        max_index = 0
        for i in range(len(bank) - 1):
            if bank[i] > d1:
                max_index = i
                d1 = bank[i]

        d2 = 0
        for i in range(max_index + 1, len(bank)):
            if bank[i] > d2:
                d2 = bank[i]

        num += d1 * 10 + d2

        sum += num

    return sum


def part2(input_data):
    banks = parse_input(input_data)

    sum = 0

    for bank in banks:
        remaining = len(bank) - 12
        stack = []

        for b in bank:
            while remaining > 0 and len(stack) > 0 and stack[-1] < b:
                stack.pop()
                remaining -= 1

            stack.append(b)

        if len(stack) > 12:
            stack = stack[:12]

        max_num = int("".join(map(str, stack)))

        sum += max_num

    return sum


if __name__ == "__main__":
    with open("03/sample.txt") as f:
        input_data = f.read()
        p1_sample = part1(input_data)
        print(f"Part1 sample: {p1_sample}")
        assert p1_sample == 357

        p2_sample = part2(input_data)
        print(f"Part2 sample: {p2_sample}")
        assert p2_sample == 3121910778619

    with open("03/input.txt") as f:
        input_data = f.read()
        p1_input = part1(input_data)
        print(f"Part1 input: {p1_input}")
        assert p1_input == 17085

        p2_input = part2(input_data)
        print(f"Part2 input: {p2_input}")
        assert p2_input == 169408143086082
