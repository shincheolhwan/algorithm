import sys


def dfs(cur_x, cur_y):
    global answer
    answer = max(answer, len(alphabets))

    for dx, dy in zip(dxs, dys):
        next_x, next_y = cur_x + dx, cur_y + dy

        if next_x < 0 or next_x >= R or next_y < 0 or next_y >= C:
            continue

        if board[next_x][next_y] not in alphabets:
            alphabets.add(board[next_x][next_y])
            dfs(next_x, next_y)
            alphabets.remove(board[next_x][next_y])


R, C = map(int, sys.stdin.readline().strip().split())
board = []

for _ in range(R):
    row = list(sys.stdin.readline().strip())
    board.append(row)

answer = 0
alphabets = {board[0][0]}
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

dfs(0, 0)
print(answer)
