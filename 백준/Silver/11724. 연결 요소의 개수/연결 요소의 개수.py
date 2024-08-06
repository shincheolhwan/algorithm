import sys
from queue import Queue

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = {}
for i in range(1, N + 1):
    graph[i] = set()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].add(b)
    graph[b].add(a)

count = 0
visited = set()
for i in range(1, N + 1):
    if i not in visited:
        visited.add(i)
        count += 1
        q = Queue()
        q.put(i)

        while True:
            if q.empty():
                break

            for _ in range(q.qsize()):
                cur = q.get()

                for next_node in graph[cur]:
                    if next_node not in visited:
                        visited.add(next_node)
                        q.put(next_node)

print(count)
