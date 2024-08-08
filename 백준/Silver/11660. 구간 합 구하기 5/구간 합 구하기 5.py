import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = []
dp = [[0] * (N + 1)]

for _ in range(N):
    nums.append(list(map(int, sys.stdin.readline().strip().split())))
    dp.append([0] * (N + 1))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 and j == 1:
            dp[i][j] = nums[i - 1][j - 1]
        elif i == 1:
            dp[i][j] = dp[i][j - 1] + nums[i - 1][j - 1]
        elif j == 1:
            dp[i][j] = dp[i - 1][j] + nums[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + nums[i - 1][j - 1] - dp[i - 1][j - 1]

for _ in range(M):
    start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().strip().split())
    start_x -= 1
    start_y -= 1
    print(dp[end_x][end_y] - dp[start_x][end_y] - dp[end_x][start_y] + dp[start_x][start_y])
