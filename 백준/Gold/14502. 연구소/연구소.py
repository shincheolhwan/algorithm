import sys
import queue
import itertools

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def bfs(m):
    q = queue.Queue()

    for virus in virus_points:
        q.put(virus)

    while True:
        if q.empty():
            break

        cur_x, cur_y = q.get()

        for dx, dy in zip(dxs, dys):
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < N and 0 <= next_y < M:
                if m[next_x][next_y] == 0:
                    m[next_x][next_y] = 2
                    q.put((next_x, next_y))

    count = 0
    for x in range(N):
        for y in range(M):
            if m[x][y] == 0:
                count += 1
    return count


def map_copy():
    new_map = []
    for i in range(N):
        new_map.append(maps[i].copy())
    return new_map


N, M = map(int, sys.stdin.readline().strip().split())

maps = []
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().strip().split())))

safety_points = []
virus_points = []

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            safety_points.append((i, j))
        elif maps[i][j] == 2:
            virus_points.append((i, j))

answer = 0
for combi in list(itertools.combinations(safety_points, 3)):
    new_maps = map_copy()
    for x, y in combi:
        new_maps[x][y] = 1

    answer = max(answer, bfs(new_maps))
print(answer)
