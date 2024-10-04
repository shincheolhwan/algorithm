import sys
import math
import heapq

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]


def find_fish(x, y):
    visited = [[False for _ in range(N)] for _ in range(N)]
    find = False
    find_count = math.inf
    find_x = -1
    find_y = -1
    pq = [(0, x, y)]

    while True:
        if len(pq) == 0:
            break

        count, cur_x, cur_y = heapq.heappop(pq)
        if count + 1 > find_count:
            break

        if visited[cur_x][cur_y]:
            continue
        visited[cur_x][cur_y] = True

        for dx, dy in zip(dxs, dys):
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < N and 0 <= next_y < N:
                if visited[next_x][next_y]:
                    continue
                if 0 < maps[next_x][next_y] < size:
                    if find:
                        if find_x > next_x or (find_x == next_x and find_y > next_y):
                            find_x = next_x
                            find_y = next_y
                    else:
                        find = True
                        find_count = count + 1
                        find_x = next_x
                        find_y = next_y

                elif maps[next_x][next_y] == 0 or maps[next_x][next_y] == size:
                    heapq.heappush(pq, (count + 1, next_x, next_y))

    return find, find_count, find_x, find_y


N = int(sys.stdin.readline().strip())
maps = []
cur_x, cur_y = -1, -1
time = 0
size = 2
eat_count = 0

for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().strip().split())))
    for j in range(N):
        if maps[i][j] == 9:
            cur_x, cur_y = i, j
            maps[i][j] = 0

while True:
    find, count, next_x, next_y = find_fish(cur_x, cur_y)
    if not find:
        break
    eat_count += 1
    if eat_count % size == 0:
        eat_count = 0
        size += 1
    time += count
    maps[next_x][next_y] = 0
    cur_x, cur_y = next_x, next_y

print(time)
