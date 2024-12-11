import math

from utilities import read_file

def del_last_if_point(arr):
    del arr[-1]
    if arr[-1] == ".":
        arr = del_last_if_point(arr)
    return arr

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


arr = []
for e in new_line:
    if e == ".":
        arr.append(e)
    else:
        arr.append(int(e))

print("Sort array...")


for i, e in enumerate(arr):
    if arr[-1] == ".":
        arr = del_last_if_point(arr)
    if e == ".":
        arr[i] = arr[-1]
        del arr[-1]


print(f"Array sorted!\n\n{arr}\n\nCalculation sum...")
sum = 0
for i, e in enumerate(arr):
    if e == ".":
        continue
    sum += e * i
print("Calculated sum:", sum)
