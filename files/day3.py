filename = "inputs/day_3_1.txt"
def part_1():
    with open(filename, 'r') as file:
        total = 0
        for line in file:
            line_largest = 0
            for c1 in range(len(line) - 1):
                for c2 in range(c1 + 1, len(line)):
                    s = line[c1] + line[c2]
                    if int(s) > line_largest:
                        line_largest = int(s)
            total += line_largest
        print(total)

def part_2():
    with open(filename, 'r') as file:
        total = 0
        for line in file:
            line_largest = ""
            start = 0
            line = line.strip()
            for r in range(12, 0, -1):
                end = len(line) - r
                best_n = max(line[start:end+1])
                best_i = line.index(best_n, start, end+1)
                line_largest += best_n
                start = best_i + 1
            total += int(line_largest)

        print(total)

if __name__ == "__main__":
    part_1()
    part_2()