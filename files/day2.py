filename = "inputs/day2_1.txt"

with open(filename, 'r') as file:
    ranges = file.readline().strip().split(",")
    for i in range(len(ranges)):
        ranges[i] = ranges[i].split("-")
    combos = set()
    for r in ranges:
        start = int(r[0])
        end = int(r[1])
        s = len(str(start))
        e = len(str(end))
        for l in range(s, e + 1):
            if l % 2 != 0:
                continue
            half_length = l // 2
            min_half = 10**(half_length - 1)
            max_half = (10**half_length) - 1
            for half in range(min_half, max_half + 1):
                full = int(str(half) + str(half))
                if start <= full <= end:
                    combos.add(full)
    print(sum(combos))

def divisors(n):
    return [i for i in range(1, n) if n % i == 0]

with open(filename, 'r') as file:
    ranges = file.readline().strip().split(",")
    for i in range(len(ranges)):
        ranges[i] = ranges[i].split("-")
    combos = set()
    for r in ranges:
        start = int(r[0])
        end = int(r[1])
        s = len(str(start))
        e = len(str(end))
        for l in range(s, e + 1):
            for k in divisors(l):
                repeats = l // k
                min_block = 10**(k-1)
                max_block = (10**k)-1
                for b in range(min_block, max_block + 1):
                    full = int(str(b) * repeats)
                    if start <= full <= end:
                        combos.add(full)
    print(sum(combos))

