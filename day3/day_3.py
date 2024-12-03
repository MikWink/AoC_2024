from utilities import read_file

def get_real_muls(line):
    do = True
    muls = []
    for i, char in enumerate(line):
        if i >= len(line) - 7:
            break
        if line[i:i+4] == "do()":
            do = True
        if line[i:i+7] == "don't()":
            do = False
        if line[i:i+4] == "mul(" and do:
            mul_ex = line[i:i+12]
            if ")" in mul_ex:
                for i, _ in enumerate(mul_ex):
                    if mul_ex[i] == ")":
                        if "," in mul_ex[:i+1]:
                            print(mul_ex[:i+1])
                            muls.append(mul_ex[:i+1])
                        break
    return muls

def do_muls(muls):
    sum = 0
    for mul in muls:
        nums = mul[4:-1]
        print(nums)
        left, right = nums.split(",")
        sum += int(left) * int(right)
    return sum

input = read_file("input.txt");
line = input[0]

muls = get_real_muls(input[0])
result = do_muls(muls)

print(result)


