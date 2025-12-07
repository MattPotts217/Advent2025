filename = "inputs/day6_example.txt"

def part1():
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append([x for x in line.strip().split(" ")])
    grand_total = 0
    for i in range(0, len(lines[0])):
        nums = []
        for j in range(0, len(lines) - 1):
            nums.append(int(lines[j][i]))
        if (lines[len(lines) - 1][i] == "+"):
            grand_total += sum(nums)
        else:
            total = nums[0]
            for n in range(1, len(nums)):
                total *= nums[n]
            grand_total += total
    print(grand_total)

if __name__ == "__main__":
    part1()