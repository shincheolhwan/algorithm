sudoku = []
zeros = []
row_checks = [set() for _ in range(9)]
col_checks = [set() for _ in range(9)]
square_checks = [set() for _ in range(9)]


def solve(zero_index):
    if zero_index == len(zeros):
        return True

    cur_x, cur_y = zeros[zero_index]

    for num in range(1, 10):
        if (
                num not in row_checks[cur_x] and
                num not in col_checks[cur_y] and
                num not in square_checks[find_square(cur_x, cur_y)]
        ):
            row_checks[cur_x].add(num)
            col_checks[cur_y].add(num)
            square_checks[find_square(cur_x, cur_y)].add(num)
            sudoku[cur_x][cur_y] = num
            if solve(zero_index + 1):
                return True
            row_checks[cur_x].remove(num)
            col_checks[cur_y].remove(num)
            square_checks[find_square(cur_x, cur_y)].remove(num)
            sudoku[cur_x][cur_y] = 0
    return False


def find_square(x, y):
    if 0 <= x < 3 and 0 <= y < 3:
        return 0
    elif 0 <= x < 3 and 3 <= y < 6:
        return 1
    elif 0 <= x < 3 and 6 <= y < 9:
        return 2
    elif 3 <= x < 6 and 0 <= y < 3:
        return 3
    elif 3 <= x < 6 and 3 <= y < 6:
        return 4
    elif 3 <= x < 6 and 6 <= y < 9:
        return 5
    elif 6 <= x < 9 and 0 <= y < 3:
        return 6
    elif 6 <= x < 9 and 3 <= y < 6:
        return 7
    elif 6 <= x < 9 and 6 <= y < 9:
        return 8


for _ in range(9):
    sudoku.append(list(map(int, list(input()))))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i, j))
        else:
            row_checks[i].add(sudoku[i][j])
            col_checks[j].add(sudoku[i][j])
            square_checks[find_square(i, j)].add(sudoku[i][j])

solve(0)
for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end='')
    if i != 8:
        print()
