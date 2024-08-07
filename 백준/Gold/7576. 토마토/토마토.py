from queue import Queue
import sys

M, N = map(int, sys.stdin.readline().rstrip().split())
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
tomatoes = []
q = Queue()
count = 0
for i in range(N):
    tomatoes.append([])
    row = list(map(int, sys.stdin.readline().strip().split()))

    for j, tomato in enumerate(row):
        if tomato == 1:
            q.put((i, j))
        tomatoes[i].append(tomato)

while True:
    if q.empty():
        break
    count += 1

    for _ in range(q.qsize()):
        (cur_x, cur_y) = q.get()

        for (dx, dy) in zip(dxs, dys):
            new_x: int = cur_x + dx
            new_y: int = cur_y + dy

            if 0 <= new_x < N and 0 <= new_y < M:
                if tomatoes[new_x][new_y] == 0:
                    tomatoes[new_x][new_y] = 1
                    q.put((new_x, new_y))

exist = False
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            exist = True
            break
    if exist:
        break

if exist:
    print(-1)
else:
    print(count - 1)
