#! /usr/bin/env python3


def parse_input(input_data):
    tiles = []
    lines = input_data.splitlines()
    for line in lines:
        line = line.strip()
        if line == "":
            continue

        parts = line.split(",")
        tiles.append((int(parts[0]), int(parts[1])))

    return tiles


def solve_part1(input_data):
    tiles = parse_input(input_data)

    max_area = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            xx = abs(tiles[i][0] - tiles[j][0]) + 1
            yy = abs(tiles[i][1] - tiles[j][1]) + 1
            area = xx * yy
            if area > max_area:
                max_area = area

    return max_area


if __name__ == "__main__":
    with open("09/sample.txt") as f:
        input_data = f.read()
        p1_sample = solve_part1(input_data)
        print(f"Part1 sample: {p1_sample}")
        assert p1_sample == 50

    with open("09/input.txt") as f:
        input_data = f.read()
        p1_input = solve_part1(input_data)
        print(f"Part1 input: {p1_input}")
        assert p1_input == 4749929916
