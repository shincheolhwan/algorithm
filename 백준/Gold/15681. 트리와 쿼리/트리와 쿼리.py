import sys

sys.setrecursionlimit(10 ** 6)


def makeTree(parent, cur):
    for next_node in path[cur]:
        if next_node != parent:
            makeTree(cur, next_node)
            children[cur].add(next_node)


def setCount(cur):
    for child in children[cur]:
        setCount(child)
        counts[cur] += counts[child]


N, R, Q = map(int, sys.stdin.readline().strip().split())

path = {i: set() for i in range(1, N + 1)}

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    path[a].add(b)
    path[b].add(a)

children = [set() for i in range(N + 1)]
makeTree(-1, R)

counts = [1] * (N + 1)
setCount(R)

for _ in range(Q):
    U = int(sys.stdin.readline().strip())
    print(counts[U])
