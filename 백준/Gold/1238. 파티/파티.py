import sys
import math
from queue import PriorityQueue


def dijkstra(graph, start):
    dp = [math.inf] * N
    dp[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))

    while True:
        if pq.empty():
            break

        cur_cost, cur_node = pq.get()
        if cur_cost > dp[cur_node]:
            continue

        for next_node in graph[cur_node]:
            new_cost = cur_cost + graph[cur_node][next_node]
            if new_cost < dp[next_node]:
                dp[next_node] = new_cost
                pq.put((new_cost, next_node))

    return dp


N, M, X = map(int, sys.stdin.readline().strip().split())
roads = {i: {} for i in range(N)}
reversed_roads = {i: {} for i in range(N)}

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    roads[a - 1][b - 1] = c
    reversed_roads[b - 1][a - 1] = c

come_costs = dijkstra(roads, X - 1)
back_costs = dijkstra(reversed_roads, X - 1)

answer = -1
for i in range(N):
    answer = max(answer, come_costs[i] + back_costs[i])

print(answer)
