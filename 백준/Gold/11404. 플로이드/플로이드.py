import sys
import math


def floyd_warshall():
    dp = [[math.inf] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = graph[i].get(j, math.inf)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    return dp


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {i: {} for i in range(n)}

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a - 1][b - 1] = min(graph[a - 1].get(b - 1, 100_000), c)

result = floyd_warshall()

for row in result:
    print(str(row)[1:-1].replace(",", "").replace("inf", "0"))
