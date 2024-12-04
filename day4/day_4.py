from utilities import read_file

field = read_file("input.txt")



def check_horizontal(field):
    count = 0
    for i, row in enumerate(field):
        for j, char in enumerate(row):
            if row[j:j+4] == "XMAS":
                count += 1
            elif row[j:j+4] == "SAMX":
                count += 1
    return count

def check_vertical(field):
    count = 0
    ver_index = 0
    hor_index = 0
    new_field = []
    while(hor_index < len(field[0])):
        ver_line = ""
        for i, rows in enumerate(field):
            ver_line += rows[ver_index]
        new_field.append(ver_line)
        hor_index += 1
        ver_index += 1


    return check_horizontal(new_field)

def check_one_diagonal(field):
    diagonals = []
    diagonal = ""
    for j in range(len(field)):
        for i in range(len(field) - j):
            diagonal += field[i][i + j]

        diagonals.append(diagonal)
        diagonal = ""

    rev_field = []
    for row in reversed(field):
        rev_field.append(row[::-1])

    for j in range(1, len(rev_field)):
        for i in range(len(rev_field) - j):
            diagonal += rev_field[i][i + j]

        diagonals.append(diagonal)
        diagonal = ""
    return check_horizontal(diagonals)

def check_diagonal(field):
    count = 0
    count += check_one_diagonal(field)

    rev_row_field = []
    for row in field:
        rev_row_field.append(row[::-1])


    count += check_one_diagonal(rev_row_field)



    return count

print("Vertical count: ", check_vertical(field))
print("Horizontal count: ", check_horizontal(field))
print("Diagonal count: ", check_diagonal(field))
print("Sum: ", check_horizontal(field) + check_vertical(field) + check_diagonal(field))