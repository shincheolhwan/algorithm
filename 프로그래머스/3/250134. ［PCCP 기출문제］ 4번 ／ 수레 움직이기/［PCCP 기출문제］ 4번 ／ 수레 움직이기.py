from queue import Queue

n, m = 0, 0


def solution(maze):
    global n, m
    n = len(maze)
    m = len(maze[0])
    red_start = find_index(maze, 1)
    blue_start = find_index(maze, 2)
    return bfs(red_start, blue_start, maze)


# 위 오 아 왼
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def bfs(red_start, blue_start, maze):
    path = []
    queue = Queue()
    queue.put([[red_start], [blue_start]])

    while True:
        if queue.qsize() == 0:
            break

        cur_red_path, cur_blue_path = queue.get()
        for i in range(4):
            cur_red_x = cur_red_path[-1][0]
            cur_red_y = cur_red_path[-1][1]

            # 이미 도착한 경우
            if maze[cur_red_x][cur_red_y] == 3:
                next_red_x = cur_red_x
                next_red_y = cur_red_y
            else:
                next_red_x = cur_red_x + dxs[i]
                next_red_y = cur_red_y + dys[i]
                # 넘어간 경우
                if next_red_x < 0 or next_red_x >= n or next_red_y < 0 or next_red_y >= m:
                    continue
                # 벽인 경우
                if maze[next_red_x][next_red_y] == 5:
                    continue
                # 이미 방문한 경우
                if (next_red_x, next_red_y) in cur_red_path:
                    continue

            for j in range(4):
                cur_blue_x = cur_blue_path[-1][0]
                cur_blue_y = cur_blue_path[-1][1]

                # 이미 도착한 경우
                if maze[cur_blue_x][cur_blue_y] == 4:
                    next_blue_x = cur_blue_x
                    next_blue_y = cur_blue_y
                else:
                    next_blue_x = cur_blue_x + dxs[j]
                    next_blue_y = cur_blue_y + dys[j]
                    # 넘어간 경우
                    if next_blue_x < 0 or next_blue_x >= n or next_blue_y < 0 or next_blue_y >= m:
                        continue
                    # 벽인 경우
                    if maze[next_blue_x][next_blue_y] == 5:
                        continue
                    # 이미 방문한 경우
                    if (next_blue_x, next_blue_y) in cur_blue_path:
                        continue
                # 다음 위치가 같은 경우
                if (next_red_x, next_red_y) == (next_blue_x, next_blue_y):
                    continue
                # 서로 위치가 바뀌는 경우
                if ((cur_red_x, cur_red_y) == (next_blue_x, next_blue_y)
                        and (cur_blue_x, cur_blue_y) == (next_red_x, next_red_y)):
                    continue

                next_red_path = cur_red_path.copy()
                next_blue_path = cur_blue_path.copy()

                if (cur_red_x, cur_red_y) != (next_red_x, next_red_y):
                    next_red_path.append((next_red_x, next_red_y))

                if (cur_blue_x, cur_blue_y) != (next_blue_x, next_blue_y):
                    next_blue_path.append((next_blue_x, next_blue_y))
                    
                if maze[next_red_x][next_red_y] == 3 and maze[next_blue_x][next_blue_y] == 4:
                    return max(len(next_red_path), len(next_blue_path)) - 1
                else:
                    queue.put([next_red_path, next_blue_path])

    return 0


def find_index(maze, item):
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == item:
                return i, j


# print(solution([[1, 4], [0, 0], [2, 3]]), 3)
# print(solution([[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]]), 7)
# print(solution([[1, 5], [2, 5], [4, 5], [3, 5]]), 0)
# print(solution([[4, 1, 2, 3]]), 0)
