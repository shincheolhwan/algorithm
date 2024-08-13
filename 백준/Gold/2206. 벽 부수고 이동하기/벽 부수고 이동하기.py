import sys
import math
from queue import Queue


def bfs():
    if N == 1 and M == 1:
        return 1

    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]

    dp1 = [[math.inf] * M for _ in range(N)]
    dp1[0][0] = 1
    dp2 = [[math.inf] * M for _ in range(N)]
    dp2[0][0] = 1

    count = 1
    q = Queue()
    q.put((0, 0, False))

    while True:
        if q.empty():
            break

        for _ in range(q.qsize()):
            cur_x, cur_y, broken = q.get()

            for dx, dy in zip(dxs, dys):
                next_x = cur_x + dx
                next_y = cur_y + dy

                if next_x == N - 1 and next_y == M - 1:
                    # print("dp1")
                    # for row in dp1:
                    #     print(*row)
                    # print("dp2")
                    # for row in dp2:
                    #     print(*row)
                    return count + 1
                if 0 <= next_x < N and 0 <= next_y < M:
                    if broken:
                        if (maps[next_x][next_y] == 0 and
                                dp1[next_x][next_y] > count + 1 and
                                dp2[next_x][next_y] > count + 1):
                            dp2[next_x][next_y] = count + 1
                            q.put((next_x, next_y, True))
                            continue
                    else:
                        if (maps[next_x][next_y] == 1 and
                                dp1[next_x][next_y] > count + 1 and
                                dp2[next_x][next_y] > count + 1):
                            dp2[next_x][next_y] = count + 1
                            q.put((next_x, next_y, True))
                            continue

                        if maps[next_x][next_y] == 0 and dp1[next_x][next_y] > count + 1:
                            dp1[next_x][next_y] = count + 1
                            q.put((next_x, next_y, False))
        count += 1

    return -1


N, M = map(int, sys.stdin.readline().strip().split())
maps = []

for _ in range(N):
    maps.append([int(num) for num in list(sys.stdin.readline().strip())])

print(bfs())
