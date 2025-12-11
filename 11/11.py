#!/usr/bin/env python3


def parse_input(input_data):
    graph = {}
    for line in input_data.splitlines():
        line = line.strip()
        if not line:
            continue

        source, targets = line.split(": ")

        targets = targets.split(" ")

        graph[source] = targets

    return graph


def find_path(graph, source, target, paths, path=[]):
    path = path + [source]

    if source == target:
        path = path + [target]
        paths.add("-".join(path))
        return

    for node in graph[source]:
        if node not in path:
            find_path(graph, node, target, paths, path)


def solve_part1(graph):
    paths = set()

    find_path(graph, "you", "out", paths, [])

    return len(paths)


if __name__ == "__main__":
    with open("11/sample.txt", "r") as f:
        input_data = f.read()
        graph = parse_input(input_data)

        sample1_result = solve_part1(graph)
        print(f"Sample 1: {sample1_result}")
        assert sample1_result == 5

    with open("11/input.txt", "r") as f:
        input_data = f.read()
        graph = parse_input(input_data)

        input1_result = solve_part1(graph)
        print(f"Input 1: {input1_result}")
        assert input1_result == 714
