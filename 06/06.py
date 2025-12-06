#! /usr/bin/env python3


def parse_input(input_data):
    lines = input_data.splitlines()

    rows = []
    for line in lines:
        if line == "":
            continue

        rows.append([c for c in line.split() if c != ""])

    return rows


def solve_part1(input_data):
    rows = parse_input(input_data)

    sum = 0

    for col in range(len(rows[0])):
        acc = int(rows[0][col])

        oper = rows[len(rows) - 1][col]

        for row in range(1, len(rows) - 1):
            if oper == "+":
                acc += int(rows[row][col])
            elif oper == "*":
                acc *= int(rows[row][col])

        sum += acc

    return sum


def solve_part2(input_data):
    matrix = []

    for l in input_data.splitlines():
        matrix.append([c for c in l])

    rot_matrix = [[None] * len(matrix) for _ in range(len(matrix[0]))]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rot_matrix[col][row] = matrix[row][col]

    sum = 0
    acc = None

    for row in range(len(rot_matrix)):
        # start new operation
        if rot_matrix[row][len(rot_matrix[row]) - 1].strip() != "":
            oper = rot_matrix[row][len(rot_matrix[row]) - 1]
            acc = int("".join(rot_matrix[row][0 : len(rot_matrix[row]) - 1]).strip())
        elif "".join(rot_matrix[row][0 : len(rot_matrix[row]) - 1]).strip() != "":
            # continue current operation
            num = int("".join(rot_matrix[row][0 : len(rot_matrix[row]) - 1]).strip())
            if oper == "+":
                acc += num
            elif oper == "*":
                acc *= num
        else:
            # empty column
            sum += acc
            acc = None

    # final operation
    if acc is not None:
        sum += acc

    return sum


if __name__ == "__main__":
    with open("06/sample.txt") as f:
        input_data = f.read()
        p1_sample = solve_part1(input_data)
        print(f"Part1 sample: {p1_sample}")
        assert p1_sample == 4277556

        p2_sample = solve_part2(input_data)
        print(f"Part2 sample: {p2_sample}")
        assert p2_sample == 3263827

    with open("06/input.txt") as f:
        input_data = f.read()
        p1_input = solve_part1(input_data)
        print(f"Part1 input: {p1_input}")
        assert p1_input == 6209956042374

        p2_input = solve_part2(input_data)
        print(f"Part2 input: {p2_input}")
        assert p2_input == 12608160008022
