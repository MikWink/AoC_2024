from utilities import read_file


def get_input_arr():
    input = read_file("input.txt")
    return [[int(char) for char in line.strip()] for line in input]


def find_unique_nines(input_arr, i, j, current, visited, nines_found):
    # Directions: right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Base case: If the current height is 9, add to nines_found and stop further exploration
    if current == 9:
        nines_found.add((i, j))
        return

    visited.add((i, j))  # Mark the current cell as visited

    for di, dj in directions:
        new_i, new_j = i + di, j + dj

        # Ensure the new position is within bounds and not visited
        if (0 <= new_i < len(input_arr) and
                0 <= new_j < len(input_arr[0]) and
                (new_i, new_j) not in visited and
                input_arr[new_i][new_j] == current + 1):
            find_unique_nines(input_arr, new_i, new_j, current + 1, visited, nines_found)

    visited.remove((i, j))  # Unmark the cell after exploring all paths


input_arr = get_input_arr()
trailheads_sum = 0

for i in range(len(input_arr)):
    for j in range(len(input_arr[0])):
        if input_arr[i][j] == 0:  # Trailhead starts at height 0
            visited = set()  # Track visited cells for each trailhead
            nines_found = set()  # Store unique endpoints (height 9)
            find_unique_nines(input_arr, i, j, 0, visited, nines_found)
            trailheads = len(nines_found)  # Count unique reachable `9`s
            trailheads_sum += trailheads
            print(f"Trailhead at ({i}, {j}) has {trailheads} 9 in reach.")

print(f"Total trailheads score: {trailheads_sum}")
