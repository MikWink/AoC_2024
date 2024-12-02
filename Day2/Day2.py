from utilities import read_file

def check_sequence(lst):
    # Check if numbers are increasing with valid differences
    is_increasing = all(1 <= lst[i+1] - lst[i] <= 3 for i in range(len(lst) - 1))
    # Check if numbers are decreasing with valid differences
    is_decreasing = all(1 <= lst[i] - lst[i+1] <= 3 for i in range(len(lst) - 1))
    # Return true if either condition is satisfied
    return is_increasing or is_decreasing

reports = read_file("input.txt")
count = 0

for rep in reports:
    report = list(map(int, rep.split()))
    if check_sequence(report):
        count += 1


print(count)