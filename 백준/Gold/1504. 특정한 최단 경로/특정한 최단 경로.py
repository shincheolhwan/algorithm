# 1 -> v1 -> v2 -> N
# or 1 -> v2 -> v1 -> N

# 1에서 다익
# v1에서 다익
# v2에서 다익
import sys
import math
import heapq


def dijkstra(graph, start):
    dp = [math.inf] * (N + 1)
    pq = []
    heapq.heappush(pq, (0, start))

    while True:
        if len(pq) == 0:
            break

        cost, cur = heapq.heappop(pq)
        if dp[cur] <= cost:
            continue

        dp[cur] = cost
        for nxt in graph[cur]:
            new_cost = cost + graph[cur][nxt]
            if new_cost < dp[nxt]:
                heapq.heappush(pq, (new_cost, nxt))

    return dp


N, E = map(int, sys.stdin.readline().strip().split())

graph = {i: {} for i in range(1, N + 1)}

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, sys.stdin.readline().strip().split())
dp1 = dijkstra(graph, 1)
dp2 = dijkstra(graph, v1)
dp3 = dijkstra(graph, v2)

answer = min(dp1[v1] + dp2[v2] + dp3[N], dp1[v2] + dp3[v1] + dp2[N])

if answer == math.inf:
    print(-1)
else:
    print(answer)
