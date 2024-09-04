import sys

N, M = map(int, sys.stdin.readline().strip().split())
memory = list(map(int, sys.stdin.readline().strip().split()))
cost = list(map(int, sys.stdin.readline().strip().split()))

dp = [0] * (100 * N + 1)

for i in range(N):
    cur_memory = memory[i]
    cur_cost = cost[i]
    for j in range(len(dp) - 1, cur_cost - 1, -1):
        dp[j] = max(dp[j], dp[j - cur_cost] + cur_memory)

for i in range(len(dp)):
    if dp[i] >= M:
        print(i)
        break
