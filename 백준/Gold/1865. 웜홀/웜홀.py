import sys


def bellman_ford(paths):
    dp = [1e9] * (N + 1)

    for r in range(1, N + 1):
        for (start, end) in paths:
            cost = paths[(start, end)]

            if dp[end] > dp[start] + cost:
                dp[end] = dp[start] + cost

                if r == N:
                    return True

    return False


TC = int(sys.stdin.readline().strip())

for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().strip().split())
    paths = {}

    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().strip().split())
        paths[(S, E)] = min(paths.get((S, E), 10_000), T)
        paths[(E, S)] = min(paths.get((E, S), 10_000), T)

    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().strip().split())
        paths[(S, E)] = min(paths.get((S, E), 10_000), -T)

    result = bellman_ford(paths)
    print("YES" if result else "NO")
