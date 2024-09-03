import sys
from queue import Queue

N, M = map(int, sys.stdin.readline().strip().split())

answer = []
q = Queue()
in_degree = [0] * (N + 1)
path = {i: set() for i in range(1, N + 1)}

for _ in range(M):
    A, B = map(int, sys.stdin.readline().strip().split())
    in_degree[B] += 1
    path[A].add(B)

for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.put(i)

while True:
    if q.empty():
        break

    cur = q.get()
    answer.append(cur)
    for nxt in path[cur]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            q.put(nxt)

print(*answer)
