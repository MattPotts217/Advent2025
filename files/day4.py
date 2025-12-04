filename = "inputs/day4.txt"

def part1():
    with open(filename, 'r') as file:
        grid = file.read().split("\n")
        grid = [list(row) for row in grid]
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ".":
                    continue
                count = 0
                for dy, dx in directions:
                    if i + dy < 0 or i + dy >= len(grid) or j + dx < 0 or j + dx >= len(grid[0]):
                        continue
                    if(grid[i + dy][j+dx]) == "@":
                        count += 1
                if count < 4:
                    answer += 1
        print(answer)

def part2():
    with open(filename, 'r') as file:
        grid = file.read().split("\n")
        grid = [list(row) for row in grid]
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        answer = 0
        while(True):
            removal = []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == ".":
                        continue
                    count = 0
                    for dy, dx in directions:
                        if i + dy < 0 or i + dy >= len(grid) or j + dx < 0 or j + dx >= len(grid[0]):
                            continue
                        if(grid[i + dy][j+dx]) == "@":
                            count += 1
                    if count < 4:
                        answer += 1
                        removal.append((i, j))
            if len(removal) == 0:
                break
            for y, x in removal:
                grid[y][x] = "."
        
        print(answer)

if __name__ == "__main__":
    part1()
    part2()