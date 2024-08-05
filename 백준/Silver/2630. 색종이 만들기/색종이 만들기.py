import sys


def counter(start_x, start_y, end_x, end_y):
    color = papers[start_x][start_y]

    check = False
    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            if papers[i][j] != color:
                check = True
                break

    if check:
        half = int((end_x - start_x) / 2)
        count1 = counter(start_x, start_y, start_x + half, start_y + half)
        count2 = counter(start_x, start_y + half + 1, start_x + half, end_y)
        count3 = counter(start_x + half + 1, start_y, end_x, start_y + half)
        count4 = counter(start_x + half + 1, start_y + half + 1, end_x, end_y)

        return count1[0] + count2[0] + count3[0] + count4[0], count1[1] + count2[1] + count3[1] + count4[1]
    else:
        if color == 1:
            return 1, 0
        else:
            return 0, 1


N = int(sys.stdin.readline().strip())

papers = []
for _ in range(N):
    papers.append(list(map(int, sys.stdin.readline().strip().split())))

blue_count, white_count = counter(0, 0, N - 1, N - 1)
print(white_count)
print(blue_count)
