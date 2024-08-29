import sys
import math


def dynamic(dp, first_color):
    for i in range(1, N):
        if i == N - 1:
            for before in range(3):
                for cur in range(3):
                    if before != cur and cur != first_color:
                        dp[i][cur] = min(dp[i][cur], dp[i - 1][before] + prices[i][cur])
        else:
            for before in range(3):
                for cur in range(3):
                    if before != cur:
                        dp[i][cur] = min(dp[i][cur], dp[i - 1][before] + prices[i][cur])


N = int(sys.stdin.readline())
prices = []
for _ in range(N):
    prices.append(tuple(map(int, sys.stdin.readline().strip().split())))

dp_r = [[math.inf] * 3 for _ in range(N)]
dp_r[0][0] = prices[0][0]
dynamic(dp_r, 0)
dp_g = [[math.inf] * 3 for _ in range(N)]
dp_g[0][1] = prices[0][1]
dynamic(dp_g, 1)
dp_b = [[math.inf] * 3 for _ in range(N)]
dp_b[0][2] = prices[0][2]
dynamic(dp_b, 2)

print(min(min(dp_r[N - 1]), min(dp_g[N - 1]), min(dp_b[N - 1])))
