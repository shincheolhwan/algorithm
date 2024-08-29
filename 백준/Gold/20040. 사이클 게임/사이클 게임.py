import sys

sys.setrecursionlimit(10 ** 9)


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parents[min(x, y)] = parents[max(x, y)]


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


N, M = map(int, sys.stdin.readline().strip().split())
answer = 0
parents = [i for i in range(N)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    if find(a) == find(b):
        answer = i + 1
        break
    else:
        union(a, b)

print(answer)
