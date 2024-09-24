import sys


def div_and_conquer(n):
    if n == 1:
        m = [[0] * N for _ in range(N)]
        for row in range(N):
            for col in range(N):
                m[row][col] = matrix[row][col] % 1000
        return m
    else:
        a = div_and_conquer(n // 2)
        if n % 2 == 0:
            return mul(a, a)
        else:
            return mul(mul(a, a), matrix)


def mul(a, b):
    ab = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            for i in range(N):
                ab[row][col] += a[row][i] * b[i][col]
            ab[row][col] %= 1000
    return ab


N, B = map(int, sys.stdin.readline().strip().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().strip().split())))

answer = div_and_conquer(B)

for r in answer:
    print(*r)
