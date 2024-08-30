import sys
from queue import Queue

T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().strip().split())
    times = [0] + list(map(int, sys.stdin.readline().strip().split()))

    path = {i: set() for i in range(1, N + 1)}
    in_degree = [0] * (N + 1)

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().strip().split())
        path[a].add(b)
        in_degree[b] += 1

    q = Queue()
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.put(i)
            dp[i] = times[i]

    while True:
        if q.empty():
            break

        cur_node = q.get()
        for next_node in path[cur_node]:
            dp[next_node] = max(dp[next_node], dp[cur_node] + times[next_node])
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.put(next_node)

    W = int(sys.stdin.readline())
    print(dp[W])
