import sys

N = int(sys.stdin.readline())
A = [[1] * (N + 2)]
for _ in range(N):
    A.append([1] + list(map(int, sys.stdin.readline().strip().split())) + [1])
A.append([1] * (N + 2))

# 위 대각 왼
dp = []
for _ in range(N + 2):
    dp.append([[0, 0, 0] for _ in range(N + 2)])
dp[1][2] = [0, 0, 1]

for r in range(1, N + 1):
    for c in range(1, N + 1):
        if A[r][c] == 1:
            continue

        # 위 (r - 1, c)
        if A[r - 1][c] == 0:
            dp[r][c][0] += dp[r - 1][c][0] + dp[r - 1][c][1]

        # 대각선 (r - 1, c - 1)
        if A[r - 1][c] == 0 and A[r][c - 1] == 0 and A[r - 1][c - 1] == 0:
            dp[r][c][1] += dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]

        # 왼 (r, c - 1)
        if A[r][c - 1] == 0:
            dp[r][c][2] += dp[r][c - 1][1] + dp[r][c - 1][2]

print(sum(dp[N][N]))
