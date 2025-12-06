filename = "inputs/day5.txt"
def part1():
    with open(filename, 'r') as file:
        ranges = []
        sorted_ranges = []
        count = 0
        for line in file:
            line = line.strip()
            if line == "":
                continue
            if "-" in line:
                ranges.append(line)
            if not "-" in line:
                sorted_ranges = sorted(ranges)
            for r in sorted_ranges:
                r = r.split("-")
                i = int(line)
                if i <= int(r[1]) and i >= int(r[0]):
                    count += 1
                    break
    print(count)

def part2():
    id_diffs = set()
    ranges = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "":
                break
            start, end = map(int, line.split("-"))
            updated = True
            while updated:
                updated = False
                for r in ranges:
                    r_start, r_end = r
                    if not (end < r_start - 1 or start > r_end + 1):
                        start = min(start, r_start)
                        end = max(end, r_end)
                        ranges.remove(r)
                        updated = True
                        break

            ranges.append([start, end])

        for r in ranges:
            id_diffs.add((int(r[1]) + 1) - int(r[0]))
    print(sum(id_diffs))



if __name__ == "__main__":
    part1()
    part2()
        