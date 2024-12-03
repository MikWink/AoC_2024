from utilities import read_file

pairs = read_file("input.txt")

left = []
right = []

for pair in pairs:
    split = pair.split()
    left.append(split[0])
    right.append(split[1])

sim = 0

for loc_l in left:
    count = 0
    for loc_r in right:
        if loc_l == loc_r:
            count += 1

    sim += (int(loc_l) * count)

print(sim)