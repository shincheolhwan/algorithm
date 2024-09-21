import sys
import math
import heapq


def dijkstra(graph, start, end):
    dist = [math.inf] * (N + 1)

    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while True:
        cost, cur = heapq.heappop(pq)
        if cur == end:
            return cost

        for nxt in graph[cur]:
            new_distance = cost + graph[cur][nxt]
            if new_distance < dist[nxt]:
                dist[nxt] = new_distance
                heapq.heappush(pq, (dist[nxt], nxt))


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

path = {i: {} for i in range(1, N + 1)}

for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().strip().split())
    path[s][e] = min(c, path[s].get(e, math.inf))

s, e = map(int, sys.stdin.readline().strip().split())
answer = dijkstra(path, s, e)
print(answer)
