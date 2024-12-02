from utilities import read_file

def check_sequence(lst):
    # Check if numbers are increasing with valid differences
    is_increasing = all(1 <= lst[i+1] - lst[i] <= 3 for i in range(len(lst) - 1))
    # Check if numbers are decreasing with valid differences
    is_decreasing = all(1 <= lst[i] - lst[i+1] <= 3 for i in range(len(lst) - 1))
    # Return true if either condition is satisfied
    return is_increasing or is_decreasing

def check_sequence_with_dampener(lst):
    def is_valid_sequence(seq):
        """Check if a sequence is valid (increasing or decreasing)."""
        is_increasing = all(1 <= seq[i+1] - seq[i] <= 3 for i in range(len(seq) - 1))
        is_decreasing = all(1 <= seq[i] - seq[i+1] <= 3 for i in range(len(seq) - 1))
        return is_increasing or is_decreasing

    # Check if the sequence is already valid
    if is_valid_sequence(lst):
        return True

    # Check if removing one element makes the sequence valid
    for i in range(len(lst)):
        temp_list = lst[:i] + lst[i+1:]  # Remove one element
        if is_valid_sequence(temp_list):
            return True

    # If no single removal makes it valid, it's unsafe
    return False

reports = read_file("input.txt")
count = 0

for rep in reports:
    report = list(map(int, rep.split()))
    if check_sequence(report):
        count += 1
print("Part 1: ", count)
count = 0
for rep in reports:
    report = list(map(int, rep.split()))
    if check_sequence_with_dampener(report):
        count += 1
print("Part 2: ", count)