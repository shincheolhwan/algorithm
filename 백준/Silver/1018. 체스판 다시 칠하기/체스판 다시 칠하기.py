import sys

N, M = map(int, sys.stdin.readline().split())
boards = []

for _ in range(N):
    boards.append(list(sys.stdin.readline().rstrip()))

answer = 64
for x in range(N - 8 + 1):
    for y in range(M - 8 + 1):
        count = 0
        start = boards[x][y]
        for i in range(8):
            cur_x = x + i
            for j in range(8):
                cur_y = y + j

                if (cur_x + cur_y) % 2 == 0 and boards[cur_x][cur_y] != start:
                    count += 1
                elif (cur_x + cur_y) % 2 == 1 and boards[cur_x][cur_y] == start:
                    count += 1
        count = min(count, 64 - count)
        answer = min(answer, count)

print(answer)
