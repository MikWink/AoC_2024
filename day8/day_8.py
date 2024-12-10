import math

from utilities import read_file

def print_map(map):
    for line in map:
        print(line)

def get_antinode(v1, v2):
    # Translate the system to origin
    nv1 = [0, 0]
    nv2 = [v2[0] - v1[0], v2[1] - v1[1]]


    # Rotate 180 Deg
    radians_180 = 180 * math.pi / 180
    rv2 = [round(nv2[0] * math.cos(radians_180) - nv2[1] * math.sin(radians_180)), round(nv2[0] * math.sin(radians_180) + nv2[1] * math.cos(radians_180))]

    # Translate back to startpoint
    rv2 = [rv2[0] + v1[0], rv2[1] + v1[1]]

    return rv2

# Read input data
input = read_file("input.txt")

# Create a 2D map directly
map = [list(line) for line in input]

antennas = [[] for i in range(80)]

for i in range(len(map)):
    for j in range(len(map[0])):
        sign_number = ord(map[i][j]) - 46
        if sign_number != 0:
            antennas[sign_number].append([i, j])

count = 0
antenna_pairs = []
for frequency in antennas:
    if frequency == []:
        continue
    for i, position in enumerate(frequency):
        for j in range(len(frequency)):
            if position != frequency[j]:
                count += 1
                antenna_pairs.append(list([position, frequency[j]]))

for pair in antenna_pairs:
    antinode = get_antinode(pair[0], pair[1])
    print(antinode)
    if antinode[0] < 0 or antinode[1] < 0:
        continue
    elif antinode[0] >= len(map) or antinode[1] >= len(map[0]):
        continue
    print(len(map), len(map[0]))
    print(antinode)
    map[antinode[0]][antinode[1]] = "#"

antinodes = sum(row.count("#") for row in map)
print_map(map)
print(f"Sum of antinodes: {antinodes}")