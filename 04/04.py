#! /usr/bin/env python3


def parse_input(input_data):
    rows = []
    for line in input_data.splitlines():
        l = line.strip()
        if l == "":
            continue

        row = [int(1 if x == "@" else 0) for x in l]

        rows.append(row)

    return rows


def solve_part1(input_data):
    rows = parse_input(input_data)

    count = 0

    for y in range(0, len(rows)):
        for x in range(0, len(rows[y])):
            if rows[y][x] == 0:
                continue

            neighbors = 0

            for dy in [-1, 0, 1]:
                ny = y + dy
                if ny < 0 or ny >= len(rows):
                    continue

                for dx in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue

                    nx = x + dx
                    if nx < 0 or nx >= len(rows[y]):
                        continue

                    if rows[ny][nx] == 1:
                        neighbors += 1

            if neighbors < 4:
                count += 1

    return count


def solve_part2(input_data):
    rows = parse_input(input_data)

    removed = 0

    while True:
        new_rows = rows.copy()

        count = 0
        for y in range(0, len(rows)):
            for x in range(0, len(rows[y])):
                if rows[y][x] == 0:
                    continue

                neighbors = 0

                for dy in [-1, 0, 1]:
                    ny = y + dy
                    if ny < 0 or ny >= len(rows):
                        continue

                    for dx in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue

                        nx = x + dx
                        if nx < 0 or nx >= len(rows[y]):
                            continue

                        if rows[ny][nx] == 1:
                            neighbors += 1

                if neighbors < 4:
                    count += 1
                    new_rows[y][x] = 0

        removed += count

        rows = new_rows

        if count == 0:
            return removed


if __name__ == "__main__":
    with open("04/sample.txt") as f:
        input_data = f.read()
        part1 = solve_part1(input_data)
        print(f"Part1 sample: {part1}")
        assert part1 == 13

        part2 = solve_part2(input_data)
        print(f"Part2 sample: {part2}")
        assert part2 == 43

    with open("04/input.txt") as f:
        input_data = f.read()
        part1 = solve_part1(input_data)
        print(f"Part1 input: {part1}")
        assert part1 == 1480

        part2 = solve_part2(input_data)
        print(f"Part2 input: {part2}")
        assert part2 == 8899
