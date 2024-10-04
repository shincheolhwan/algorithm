import sys
import math
import heapq


def dijkstra(start, end):
    dp = [math.inf] * (n + 1)
    dp[start] = 0
    parents = [-1 for _ in range(n + 1)]
    pq = []
    heapq.heappush(pq, (0, start))

    while True:
        if len(pq) == 0:
            break

        cost, cur = heapq.heappop(pq)
        if dp[cur] < cost:
            continue

        for nxt, c in graph[cur]:
            new_cost = cost + c
            if new_cost < dp[nxt]:
                dp[nxt] = new_cost
                parents[nxt] = cur
                heapq.heappush(pq, (new_cost, nxt))

    cur = end
    path = []
    while True:
        if cur == -1:
            break
        path.append(cur)
        cur = parents[cur]
    path.reverse()

    return dp[end], path


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, c))

s, e = map(int, sys.stdin.readline().strip().split())
min_cost, min_path = dijkstra(s, e)

print(min_cost)
print(len(min_path))
print(' '.join(map(str, min_path)))
