import sys
from queue import PriorityQueue


def find(x):
    if union_find[x] != x:
        union_find[x] = find(union_find[x])
    return union_find[x]


def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        union_find[max(x, y)] = union_find[min(x, y)]


N, M = map(int, sys.stdin.readline().strip().split())
pq = PriorityQueue()

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    pq.put((C, A, B))

answer = 0
edge_count = 0
union_find = [i for i in range(N + 1)]
last_cost = 0

while True:
    if edge_count == N - 1:
        break

    c, a, b = pq.get()

    if find(a) != find(b):
        edge_count += 1
        union(a, b)
        answer += c
        last_cost = c

print(answer - last_cost)
