import sys
import math
from queue import PriorityQueue


def dijkstra(start):
    distances = [math.inf] * (V + 1)
    distances[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))

    while True:
        if pq.empty():
            break

        cur_distance, cur_node = pq.get()
        if distances[cur_node] < cur_distance:
            continue

        for next_node, weight in graph[cur_node]:
            new_distance = cur_distance + weight
            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                pq.put((new_distance, next_node))

    return distances


V, E = map(int, sys.stdin.readline().strip().split())
start_node = int(sys.stdin.readline().strip())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))

costs = dijkstra(start_node)
for i in range(1, V + 1):
    if costs[i] == math.inf:
        print("INF")
    else:
        print(costs[i])
