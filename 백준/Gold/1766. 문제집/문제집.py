import sys
import heapq

N, M = map(int, sys.stdin.readline().strip().split())
path = {i: set() for i in range(1, N + 1)}
in_degree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    in_degree[b] += 1
    path[a].add(b)

pq = []
answer = []

for i in range(1, N + 1):
    if in_degree[i] == 0:
        heapq.heappush(pq, i)

while True:
    if not pq:
        break

    cur = heapq.heappop(pq)
    answer.append(cur)

    for nxt in path[cur]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            heapq.heappush(pq, nxt)

print(*answer)
