import sys

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def diffusion():
    global maps

    new_maps = [[0] * C for _ in range(R)]
    new_maps[top_x][top_y] = -1
    new_maps[bottom_x][bottom_y] = -1

    for x in range(R):
        for y in range(C):
            dust = maps[x][y]

            if dust == 0 or dust == -1:
                continue

            diffuse_amount = dust // 5
            diffuse_count = 0
            for dx, dy in directions:
                next_x = x + dx
                next_y = y + dy

                if 0 <= next_x < R and 0 <= next_y < C:
                    if new_maps[next_x][next_y] == -1:
                        continue
                    new_maps[next_x][next_y] += diffuse_amount
                    diffuse_count += 1
            new_maps[x][y] += dust - diffuse_count * diffuse_amount
    maps = new_maps


def wind():
    global maps

    before = 0
    for y in range(1, C):
        temp = maps[top_x][y]
        maps[top_x][y] = before
        before = temp
    for x in range(top_x - 1, -1, -1):
        temp = maps[x][C - 1]
        maps[x][C - 1] = before
        before = temp
    for y in range(C - 2, -1, -1):
        temp = maps[0][y]
        maps[0][y] = before
        before = temp
    for x in range(1, top_x):
        temp = maps[x][0]
        maps[x][0] = before
        before = temp

    before = 0
    for y in range(1, C):
        temp = maps[bottom_x][y]
        maps[bottom_x][y] = before
        before = temp
    for x in range(bottom_x + 1, R):
        temp = maps[x][C - 1]
        maps[x][C - 1] = before
        before = temp
    for y in range(C - 2, -1, -1):
        temp = maps[R - 1][y]
        maps[R - 1][y] = before
        before = temp
    for x in range(R - 2, bottom_x, -1):
        temp = maps[x][0]
        maps[x][0] = before
        before = temp


R, C, T = map(int, sys.stdin.readline().strip().split())

maps = []
top_x = -1
top_y = 0
bottom_x = -1
bottom_y = 0

for r in range(R):
    row = list(map(int, sys.stdin.readline().strip().split()))

    if row[0] == -1:
        if top_x == -1:
            top_x = r
        else:
            bottom_x = r

    maps.append(row)

for _ in range(T):
    diffusion()
    wind()

answer = 0
for r in range(R):
    for c in range(C):
        if maps[r][c] > 0:
            answer += maps[r][c]
print(answer)
