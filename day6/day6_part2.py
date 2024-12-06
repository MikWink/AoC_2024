from utilities import read_file
import os

def get_2d_map():
    map = read_file("input.txt")
    field = []
    for line in map:
        field.append(list(line.strip()))
    return field

def get_start(map):
    for i, line in enumerate(map):
        for j, e in enumerate(line):
            if e == "<":
                return [i, j], "left"
            elif e == ">":
                return [i, j], "right"
            elif e == "^":
                return [i, j], "up"
            elif e == "v":
                return [i, j], "down"
    return None, None

def next_move_possible(position, direction, size):
    # Check if the move is out of bounds
    if direction == "up" and position[0] == 0:
        return False
    elif direction == "down" and position[0] == size-1:
        return False
    elif direction == "left" and position[1] == 0:
        return False
    elif direction == "right" and position[1] == size-1:
        return False
    return True

def move(map, position, direction):
    # Define movement based on the direction
    if direction == "up":
        if map[position[0] - 1][position[1]] != "#":
            position[0] -= 1
        else:
            direction = "right"
    elif direction == "down":
        if map[position[0] + 1][position[1]] != "#":
            position[0] += 1
        else:
            direction = "left"
    elif direction == "left":
        if map[position[0]][position[1] - 1] != "#":
            position[1] -= 1
        else:
            direction = "up"
    elif direction == "right":
        if map[position[0]][position[1] + 1] != "#":
            position[1] += 1
        else:
            direction = "down"

    #map[position[0]][position[1]] = "X"
    return position, direction

def print_map(map):
    for line in map:
        print("".join(line))
    print("\n")

map = get_2d_map()
print(f"Map shape: {len(map)}x{len(map[0])}")
startpoint, direction = get_start(map)
#map[int(startpoint[0])][int(startpoint[1])] = "X"
current_position = startpoint
moves_count = 0

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == ".":
            map[i][j] = "#"

        # Traverse until no valid move
        while next_move_possible(current_position, direction, len(map)):
            new_position, new_direction = move(map, current_position, direction)
            if current_position == new_position:
                moves_count += 1
            current_position = new_position
            direction = new_direction

        for line in map:
            lin = ""
            for l in line:
                lin += l
            print(lin)

        os.system('clear')
        map[i][j] = "."



# Count the moves
#moves = sum(row.count("X") for row in map)


#print(f"The warden takes {moves} moves to leave.")
