import os
import time
from utilities import read_file


def get_2d_map():
    # Read map only once
    return [list(line.strip()) for line in read_file("input.txt")]


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
    if direction == "up" and position[0] == 0:
        return False
    elif direction == "down" and position[0] == size - 1:
        return False
    elif direction == "left" and position[1] == 0:
        return False
    elif direction == "right" and position[1] == size - 1:
        return False
    return True


def move(map, position, direction):
    if direction == "up":
        if map[position[0] - 1][position[1]] != "#" and map[position[0] - 1][position[1]] != "O":
            position[0] -= 1
        else:
            direction = "right"
    elif direction == "down":
        if map[position[0] + 1][position[1]] != "#" and map[position[0] + 1][position[1]] != "O":
            position[0] += 1
        else:
            direction = "left"
    elif direction == "left":
        if map[position[0]][position[1] - 1] != "#" and map[position[0]][position[1] - 1] != "O":
            position[1] -= 1
        else:
            direction = "up"
    elif direction == "right":
        if map[position[0]][position[1] + 1] != "#" and map[position[0]][position[1] + 1] != "O":
            position[1] += 1
        else:
            direction = "down"

    map[position[0]][position[1]] = "X"
    return position, direction


def print_map(map):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
    for line in map:
        print("".join(line))
    print("\n")


# Initialize map once
map = get_2d_map()
loop_count = 0
count_all = 0

solution_visited = []

startpoint, direction = get_start(map)

current_position = startpoint
check = True
while check:
    check_element = [current_position, direction]  # Convert to tuple for faster set lookup
    solution_visited.append(list(current_position))
    check = next_move_possible(current_position, direction, len(map))
    if check:
        new_position, new_direction = move(map, current_position, direction)
        current_position = new_position
        direction = new_direction

# Initialize map once
map = get_2d_map()

startpoint, direction = get_start(map)

current_position = startpoint

for i in range(len(map)):
    for j in range(len(map[0])):
        count_all += 1
        print(f"{count_all}/{len(map) * len(map)}")
        if [i, j] not in solution_visited:
            continue
        visited_positions = []  # Reset for each run
        map_copy = [row[:] for row in map]  # Copy map to avoid modifying the original
        startpoint, direction = get_start(map_copy)

        if startpoint == [i, j] or startpoint == [i + 1, j]:
            continue

        map_copy[i][j] = "O"
        map_copy[int(startpoint[0])][int(startpoint[1])] = "X"
        current_position = startpoint

        loop_count_ceck = loop_count

        # Traverse until no valid move
        while next_move_possible(current_position, direction, len(map_copy)):
            check_element = [current_position, direction]  # Convert to tuple for faster set lookup
            if check_element in visited_positions:
                loop_count += 1
                print(f"loop_count: {loop_count}")
                break
            visited_positions.append([list(current_position), direction])
            solution_visited.append(list(current_position))
            new_position, new_direction = move(map_copy, current_position, direction)
            current_position = new_position
            direction = new_direction

        # Final map display - Optional for debugging purposes
        #if loop_count_ceck != loop_count:
        #    print_map(map_copy)  # Comment this out if not needed
        #time.sleep(0.2)  # Comment out if not necessary for debugging

# Final map display (after all runs)
#print_map(map_copy)
# Count the moves
moves = sum(row.count("X") for row in map_copy)
print(f"The warden takes moves {moves} to leave. At {loop_count} position is a loop created.")
