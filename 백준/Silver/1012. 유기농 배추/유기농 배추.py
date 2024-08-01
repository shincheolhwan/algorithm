from queue import Queue

T = int(input())


def solution(m, n, points):
    count = 0
    visited = set()
    maps = [[0 for _ in range(n)] for _ in range(m)]
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]

    for point in points:
        maps[point[0]][point[1]] = 1

    for i in range(m):
        for j in range(n):
            if maps[i][j] == 0:
                continue
            elif maps[i][j] == 1 and (i, j) not in visited:
                q = Queue()
                q.put((i, j))
                visited.add((i, j))
                while True:
                    if q.empty():
                        break

                    for _ in range(q.qsize()):
                        cur_x, cur_y = q.get()

                        for dx, dy in zip(dxs, dys):
                            next_x = cur_x + dx
                            next_y = cur_y + dy

                            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                                continue

                            if maps[next_x][next_y] == 0:
                                continue

                            if (next_x, next_y) in visited:
                                continue

                            q.put((next_x, next_y))
                            visited.add((next_x, next_y))

                count += 1
    return count


for _ in range(T):
    M, N, K = map(int, input().split())
    points = []
    for _ in range(K):
        x, y = map(int, input().split())
        points.append((x, y))
    print(solution(M, N, points))
