import sys

n = int(sys.stdin.readline().strip())

dp = []
triangle = []
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().strip().split())))
    dp.append([-1] * len(triangle[-1]))

dp[0][0] = triangle[0][0]

for i in range(n - 1):
    row = triangle[i]

    for j, cur in enumerate(row):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

print(max(dp[-1]))
