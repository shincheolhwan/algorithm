N = int(input())


def dfs(row, count):
    total = 0
    if count == N:
        return total + 1

    for i in range(N):
        if column_check[i] is False and inc_diagonal_check[row + i] is False and dec_diagonal_check[row - i] is False:
            column_check[i] = True
            inc_diagonal_check[row + i] = True
            dec_diagonal_check[row - i] = True
            total += dfs(row + 1, count + 1)
            column_check[i] = False
            inc_diagonal_check[row + i] = False
            dec_diagonal_check[row - i] = False

    return total


column_check = [False] * N
inc_diagonal_check = [False] * (2 * N - 1)
dec_diagonal_check = [False] * (2 * N - 1)
print(dfs(0, 0))