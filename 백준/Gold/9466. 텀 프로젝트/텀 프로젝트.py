import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    path = [0] + list(map(int, sys.stdin.readline().strip().split()))

    visited = [False] * (n + 1)
    confirmed = []

    for i in range(1, n + 1):
        cur = i
        temp = []

        while True:
            if visited[cur]:
                if cur in temp:
                    confirmed += temp[temp.index(cur):]
                break

            temp.append(cur)
            visited[cur] = True
            cur = path[cur]

    print(n - len(confirmed))
