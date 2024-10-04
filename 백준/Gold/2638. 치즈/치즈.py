import sys
from queue import Queue


def get_air_points():
    q = Queue()
    q.put((0, 0))

    while True:
        if q.empty():
            break

        cur_x, cur_y = q.get()

        for dx, dy in zip(dxs, dys):
            next_x, next_y = cur_x + dx, cur_y + dy

            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue

            if maps[next_x][next_y] == 0 and not visited[next_x][next_y]:
                q.put((next_x, next_y))
                visited[next_x][next_y] = 1
            if maps[next_x][next_y] == 1:
                visited[next_x][next_y] += 1


n, m = map(int, sys.stdin.readline().strip().split())
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
cheese_count = 0
air_point = set()
maps = []
for x in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))
    maps.append(row)

    for y in range(m):
        if row[y] == 1:
            cheese_count += 1

time = 0
while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]

    if cheese_count == 0:
        break

    get_air_points()

    for x in range(n):
        for y in range(m):
            if visited[x][y] >= 2 and maps[x][y] == 1:
                cheese_count -= 1
                maps[x][y] = 0

    time += 1

print(time)
