package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Move struct {
	Direction string
	Steps     int
}

func parseMoves(lines []string) []Move {
	var moves []Move
	for _, line := range lines {
		dir := line[0:1]
		steps, err := strconv.Atoi(line[1:])
		if err != nil {
			continue
		}
		moves = append(moves, Move{Direction: dir, Steps: steps})
	}
	return moves
}

func part1(lines []string) int {
	moves := parseMoves(lines)

	position := 50
	zeros := 0
	for _, move := range moves {
		switch move.Direction {
		case "R":
			position += move.Steps
		case "L":
			position -= move.Steps
		}
		position %= 100
		if position == 0 {
			zeros++
		}
	}
	return zeros
}

func part2(lines []string) int {
	moves := parseMoves(lines)

	position := 50
	zeros := 0

	for _, move := range moves {
		step := 0
		switch move.Direction {
		case "R":
			step = 1
		case "L":
			step = -1
		}

		for i := 0; i < move.Steps; i++ {
			position += step
			position %= 100
			if position == 0 {
				zeros++
			}
		}
	}

	return zeros
}

func main() {
	data, err := os.ReadFile("01/input.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	result1 := part1(lines)
	fmt.Println("Part 1:", result1)

	result2 := part2(lines)
	fmt.Println("Part 1:", result2)

}
