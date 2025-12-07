#!/usr/bin/env python3


def parse_input(input_data):
    lines = input_data.splitlines()

    grid = []

    start_pos = None

    row = 0
    for line in lines:
        l = line.strip()
        if l == "":
            continue

        for col, c in enumerate(l):
            if c == "S":
                start_pos = (row, col)

        grid.append([x for x in l])
        row += 1

    return (grid, start_pos)


def solve_part1(grid, start_pos):
    y_max = len(grid)
    x_max = len(grid[0])

    splits = 0

    beams = set([start_pos])
    while len(beams) > 0:
        new_beams = set()
        for beam in beams:
            new_pos = (beam[0] + 1, beam[1])

            if (
                new_pos[0] < 0
                or new_pos[0] >= y_max
                or new_pos[1] < 0
                or new_pos[1] >= x_max
            ):
                continue

            cell = grid[new_pos[0]][new_pos[1]]
            if cell == "^":
                new_beams.add((new_pos[0], new_pos[1] - 1))
                new_beams.add((new_pos[0], new_pos[1] + 1))
                splits += 1
            else:
                new_beams.add(new_pos)

        beams = new_beams

    return splits


if __name__ == "__main__":
    with open("07/sample.txt", "r") as f:
        input_data = f.read()

        grid, start_pos = parse_input(input_data)

        result_part1 = solve_part1(grid, start_pos)
        print(f"Part 1 sample: {result_part1}")
        assert result_part1 == 21

    with open("07/input.txt", "r") as f:
        input_data = f.read()

        grid, start_pos = parse_input(input_data)

        result_part1 = solve_part1(grid, start_pos)
        print(f"Part 1 input: {result_part1}")
        assert result_part1 == 1553
