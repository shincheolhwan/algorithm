import sys

N = int(sys.stdin.readline().strip())

RGBs = []
dp = []
for _ in range(N):
    RGBs.append(list(map(int, sys.stdin.readline().strip().split())))
    dp.append([-1, -1, -1])

dp[0][0] = RGBs[0][0]
dp[0][1] = RGBs[0][1]
dp[0][2] = RGBs[0][2]

for index in range(1, N):
    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            if dp[index][i] == -1:
                dp[index][i] = dp[index - 1][j] + RGBs[index][i]
            else:
                dp[index][i] = min(dp[index][i], dp[index - 1][j] + RGBs[index][i])

print(min(dp[-1]))
