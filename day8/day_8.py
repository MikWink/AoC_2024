from utilities import read_file

def print_map(map):
    for line in map:
        print(line)

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

for frequency in antennas:
    if frequency == []:
        continue
    for i, position in enumerate(frequency):
        if i == len(frequency):
            break


print_map(map)