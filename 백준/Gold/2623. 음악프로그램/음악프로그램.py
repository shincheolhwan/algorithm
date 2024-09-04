import sys
from queue import Queue

N, M = map(int, sys.stdin.readline().strip().split())

in_degree = [0] * (N + 1)
path = {i: set() for i in range(1, N + 1)}

for _ in range(M):
    order = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(1, len(order) - 1):
        cur, nxt = order[i], order[i + 1]

        if nxt not in path[cur]:
            path[cur].add(nxt)
            in_degree[nxt] += 1

q = Queue()

for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.put(i)

answer = []
while True:
    if q.empty():
        break

    cur = q.get()
    answer.append(cur)

    for nxt in path[cur]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            q.put(nxt)

if len(answer) == N:
    for i in answer:
        print(i)
else:
    print(0)
