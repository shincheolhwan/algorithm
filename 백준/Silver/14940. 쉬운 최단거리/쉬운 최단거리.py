import sys
from queue import Queue

n, m = map(int, sys.stdin.readline().strip().split())

maps = []
checks = []
start_x, start_y = -1, -1
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
for i in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))
    checks.append([-1] * m)
    maps.append(row)

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            checks[i][j] = 0
        elif maps[i][j] == 1:
            continue
        else:
            start_x, start_y = i, j
            checks[i][j] = 0

count = 0
q = Queue()
q.put((start_x, start_y))

while True:
    if q.empty():
        break
    count += 1
    for _ in range(q.qsize()):
        cur_x, cur_y = q.get()

        for (dx, dy) in zip(dxs, dys):
            next_x = cur_x + dx
            next_y = cur_y + dy

            if 0 <= next_x < n and 0 <= next_y < m:
                if checks[next_x][next_y] == -1:
                    q.put((next_x, next_y))
                    checks[next_x][next_y] = count

for row in checks:
    print(str(row)[1: -1].replace(",", ""))
