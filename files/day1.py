filename = "inputs/day1_1.txt"

with open(filename, 'r') as file:
    location = 50
    code = 0
    for line in file:
        direction = line[0]
        distance = int(line[1:])
        if direction == "L":
            location = (location - distance) % 100
        elif direction == "R":
            location = (location + distance) % 100
        if location == 0:
            code = code + 1
    print(code)

with open(filename, 'r') as file:
    location = 50
    code = 0
    for line in file:
        direction = line[0]
        distance = int(line[1:])
        if direction == "L":
            if location != 0:
                dist = location
            else:
                dist = 100
            if distance < dist:
                zero = 0
            else:
                zero = 1 + (distance - dist) // 100
            location = (location - distance) % 100
                
        elif direction == "R":
            if location != 0:
                dist = 100 - location
            else:
                dist = 100
            if distance < dist:
                zero = 0
            else:
                zero = 1 + (distance - dist) // 100
            location = (location + distance) % 100
        code = code + zero
    print(code)