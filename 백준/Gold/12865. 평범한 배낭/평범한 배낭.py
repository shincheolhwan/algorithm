import sys

N, K = map(int, sys.stdin.readline().strip().split())

items = []
dp = [0] * (K + 1)
for _ in range(N):
    items.append(tuple(map(int, sys.stdin.readline().strip().split())))

items.sort(key=lambda item: (item[0], item[1]))

for W, V in items:
    for i in range(K, W - 1, -1):
        dp[i] = max(dp[i], dp[i - W] + V)

print(dp[K])
