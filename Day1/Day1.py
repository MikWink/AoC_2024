from utilities import read_file

pairs = read_file("input.txt")

left = []
right = []

for pair in pairs:
    split = pair.split()
    left.append(split[0])
    right.append(split[1])

left.sort()
right.sort()
sum = 0

for i, loc in enumerate(left):
    distance = abs(int(loc) - int(right[i]))
    sum += distance

print(sum)