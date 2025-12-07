from collections import deque

filename = "inputs/day7.txt"

def part1():
    with open(filename, 'r') as file:
        grid = []
        splits = 0
        start = (0, 0)
        for line in file:
            grid.append([row for row in line.strip()])
        for i in range(len(grid[0])):
            if grid[0][i] == "S":
                start = (0, i)
        q = deque([start])
        visited = [start]
        while q:
            coords = q.popleft()
            if coords[0] < 0 or coords[0] >= len(grid) or coords[1] < 0 or coords[1] >= len(grid):
                continue
            if grid[coords[0]][coords[1]] == "^":
                splits += 1
                if (coords[0], coords[1] - 1) not in visited:
                    visited.append((coords[0], coords[1] - 1))
                    q.append((coords[0], coords[1] - 1))
                if (coords[0], coords[1] + 1) not in visited:
                    visited.append((coords[0], coords[1] + 1))
                    q.append((coords[0], coords[1] + 1))
            else:
                if (coords[0]+1, coords[1]) not in visited:
                    q.append((coords[0] + 1, coords[1]))
                    visited.append((coords[0] + 1, coords[1]))
        print(splits)

def part2():
    with open(filename, 'r') as file:
        grid = []
        start = (0, 0)
        for line in file:
            grid.append([row for row in line.strip()])
        for i in range(len(grid[0])):
            if grid[0][i] == "S":
                start = (0, i)
        
        memo = dict()
        def f(coords):
            nonlocal grid, memo
            if coords[0] >= len(grid):
                return 1
            if coords in memo:
                return memo[coords]
            timelines = 0
            if grid[coords[0]][coords[1]] == "^":
                timelines += f((coords[0], coords[1] - 1))
                timelines += f((coords[0], coords[1] +1))
            else:
                timelines += f((coords[0] + 1, coords[1]))
            memo[coords] = timelines
            return timelines

    print(f(start))


if __name__ == "__main__":
    part1()
    part2()