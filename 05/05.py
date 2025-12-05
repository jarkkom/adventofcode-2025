#!/usr/bin/env python3


def parse_input(input_data):
    lines = input_data.splitlines()

    ranges = []
    ingredients = []

    while True:
        line = lines.pop(0).strip()
        if line == "":
            break

        (start, end) = line.split("-")
        ranges.append((int(start), int(end)))

    while len(lines) > 0:
        line = lines.pop(0).strip()
        if line == "":
            continue

        ingredients.append(int(line))

    return (ranges, ingredients)


def solve_part1(ranges, ingredients):
    valid_ingredients = set()

    for ingredient in ingredients:
        for start, end in ranges:
            if start <= ingredient <= end:
                valid_ingredients.add(ingredient)
                break

    return len(valid_ingredients)


def solve_part2(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])

    merged_ranges = [ranges[0]]

    for start, end in ranges[1:]:
        (prev_start, prev_end) = merged_ranges[-1]

        if start <= prev_end:
            merged_ranges[-1] = (prev_start, max(prev_end, end))
        else:
            merged_ranges.append((start, end))

    count = 0
    for start, end in merged_ranges:
        count += end - start + 1

    return count


if __name__ == "__main__":
    with open("05/sample.txt", "r") as f:
        input_data = f.read()
        ranges, ingredients = parse_input(input_data)

        result_part1 = solve_part1(ranges, ingredients)
        print(f"Part 1 sample: {result_part1}")
        assert result_part1 == 3

        result_part2 = solve_part2(ranges)
        print(f"Part 2 sample: {result_part2}")
        assert result_part2 == 14

    with open("05/input.txt", "r") as f:
        input_data = f.read()
        ranges, ingredients = parse_input(input_data)

        result_part1 = solve_part1(ranges, ingredients)
        print(f"Part 1 input: {result_part1}")
        assert result_part1 == 511

        result_part2 = solve_part2(ranges)
        print(f"Part 2 input: {result_part2}")
        assert result_part2 == 350939902751909
