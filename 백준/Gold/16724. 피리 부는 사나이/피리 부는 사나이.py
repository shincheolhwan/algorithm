import sys


def move(direction, x, y):
    if direction == 'U':
        return x - 1, y
    elif direction == 'D':
        return x + 1, y
    elif direction == 'L':
        return x, y - 1
    elif direction == 'R':
        return x, y + 1


N, M = map(int, sys.stdin.readline().strip().split())
maps = []
check = [[False for _ in range(M)] for _ in range(N)]
answer = 0
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

for _ in range(N):
    maps.append(list(sys.stdin.readline().strip()))

for i in range(N):
    for j in range(M):
        x, y = i, j
        cycle = []

        while True:
            if check[x][y]:
                if (x, y) in cycle:
                    answer += 1
                break

            check[x][y] = True
            cycle.append((x, y))
            x, y = move(maps[x][y], x, y)

print(answer)
