import sys
import math
from queue import PriorityQueue


def dijkstra(start):
    distances = [math.inf] * (n + 1)
    distances[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))

    while True:
        if pq.empty():
            break
        cur_dist, cur_node = pq.get()
        if cur_dist > distances[cur_node]:
            continue
        for next_node in graph[cur_node]:
            next_dist = cur_dist + graph[cur_node][next_node]
            if next_dist < distances[next_node]:
                distances[next_node] = next_dist
                pq.put((next_dist, next_node))

    count = 0
    for i in range(1, n + 1):
        if distances[i] <= m:
            count += items[i]

    return count


n, m, r = map(int, sys.stdin.readline().strip().split())
items = [0] + list(map(int, sys.stdin.readline().strip().split()))
graph = {i: {} for i in range(1, n + 1)}

for _ in range(r):
    a, b, i = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = min(graph[a].get(b, math.inf), i)
    graph[b][a] = min(graph[b].get(a, math.inf), i)

answer = 0
for s in range(1, n + 1):
    answer = max(answer, dijkstra(s))

print(answer)
