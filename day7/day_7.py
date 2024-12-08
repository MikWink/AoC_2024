from utilities import read_file

def can_calculate(target, numbers, current_index=0, current_value=None, memo=None):
    if memo is None:
        memo = {}

    # Use the current state as a key for memoization
    state = (current_index, current_value)
    if state in memo:
        return memo[state]

    # If starting, initialize with the first number
    if current_value is None:
        current_value = numbers[current_index]
        current_index += 1

    # Base case: If we've used all numbers, check if we reached the target
    if current_index == len(numbers):
        return current_value == target

    # Recursive case: Try both + and * with the next number
    next_number = numbers[current_index]
    add_path = can_calculate(target, numbers, current_index + 1, current_value + next_number, memo)
    mult_path = can_calculate(target, numbers, current_index + 1, current_value * next_number, memo)

    # Memoize and return the result
    result = add_path or mult_path
    memo[state] = result
    return result

# Example input parsing
def process_input(input_str):
    cases = []
    in_string = ""
    for line in input_str:
        in_string += line + "\n"

    for line in in_string.strip().split("\n"):
        left, right = line.split(":")
        target = int(left)
        numbers = list(map(int, right.strip().split()))
        cases.append((target, numbers))
    return cases



input = read_file("input.txt")
cases = process_input(input)
res = 0
count = 0
# Solve each case
for target, numbers in cases:
    count += 1
    result = can_calculate(target, numbers)
    res += target if result else 0
    print(f"{count}: {target}: {'YES' if result else 'NO'}")

print(f"Result: {res}")
