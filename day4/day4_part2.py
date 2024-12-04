from utilities import read_file

field = read_file("input.txt")

def check_MAS(field, y, x):
    #Check letter top left
    if field[y-1][x-1] == "M" or field[y-1][x-1] == "S":
        if field[y+1][x+1] == "M" or field[y+1][x+1] == "S":
            if field[y-1][x-1] != field[y+1][x+1]:
                if field[y+1][x - 1] == "M" or field[y + 1][x - 1] == "S":
                    if field[y - 1][x + 1] == "M" or field[y - 1][x + 1] == "S":
                        if field[y + 1][x - 1] != field[y - 1][x + 1]:
                            print(y, x)
                            return 1

    return 0




def check_horizontal(field):
    count = 0
    for i in range(1, len(field)-1):
        for j in range(1, len(field[i])-1):
            char = field[i][j]
            if char == "A":
                count += check_MAS(field, i, j)
    return count



print("Horizontal count: ", check_horizontal(field))