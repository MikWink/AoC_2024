import math

from utilities import read_file

# Read input data
input = read_file("input.txt")

line = input[0]

new_line = ""
count = 0
for i in range(len(line)):
    if i % 2 == 0:
        for j in range(int(line[i])):
            new_line += str(count)
        count += 1
    elif i % 2 == 1:
        for j in range(int(line[i])):
            new_line += str(".")

print(new_line)