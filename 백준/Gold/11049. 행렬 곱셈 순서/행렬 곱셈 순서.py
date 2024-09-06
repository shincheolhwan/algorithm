import sys

N = int(sys.stdin.readline())

matrix = []

for _ in range(N):
    r, c = map(int, sys.stdin.readline().strip().split())
    matrix.append((r, c))

dp = [[0 for _ in range(N)] for _ in range(N)]

for count in range(1, N):
    for y in range(count, N):
        x = y - count
        dp[x][y] = 2 ** 32
        for k in range(x, y):
            dp[x][y] = min(dp[x][y], dp[x][k] + dp[k + 1][y] + matrix[x][0] * matrix[k][1] * matrix[y][1])
print(dp[0][N - 1])
