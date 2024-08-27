import sys
from queue import PriorityQueue


def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        uf[min(x, y)] = max(x, y)


def find(x):
    if uf[x] != x:
        uf[x] = find(uf[x])
    return uf[x]


V, E = map(int, sys.stdin.readline().strip().split())
pq = PriorityQueue()

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    pq.put((C, A, B))

answer = 0
edge_count = 0
uf = [i for i in range(V + 1)]

while True:
    if edge_count == V - 1:
        break

    c, a, b = pq.get()

    if find(a) != find(b):
        union(a, b)
        edge_count += 1
        answer += c

print(answer)
