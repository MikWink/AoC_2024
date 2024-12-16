from utilities import read_file

def get_input():
    input = read_file('input.txt')
    positions = []
    velocities = []
    for line in input:
        position, velocity = line.split(' ')
        positions.append(position)
        velocities.append(velocity)

    return positions, velocities

def generate_map(x, y):
    map = ['.' for _ in range(x)]
    map = [map for _ in range(y)]
    return map

def print_map(map):
    for line in map:
        for e in line:
            print(e, end='')
        print()

positions, velocities = get_input()
map = generate_map(11, 7)
print_map(map)
print(positions)
count = 0
for position in positions:
    if count == 0:
        x, y = position[2:].split(',')
        x = int(x)
        y = int(y)
        print(x, y)
        map[y][x] = "O"
    count += 1
print(map)
print_map(map)