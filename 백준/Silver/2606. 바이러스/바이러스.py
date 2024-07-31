from queue import Queue

N = int(input())
connect_count = int(input())

connection = {}
for i in range(1, N + 1):
    connection[i] = set()

for _ in range(connect_count):
    a, b = map(int, input().split())
    connection[a].add(b)
    connection[b].add(a)

visited = {1}
q = Queue()
q.put(1)

while True:
    if q.qsize() == 0:
        break

    for _ in range(q.qsize()):
        cur = q.get()
        conn = connection[cur]
        for next_computer in conn:
            if next_computer not in visited:
                visited.add(next_computer)
                q.put(next_computer)

print(len(visited) - 1)
