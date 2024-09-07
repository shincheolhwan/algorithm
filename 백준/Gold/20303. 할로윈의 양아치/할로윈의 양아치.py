import sys
import collections

N, M, K = map(int, sys.stdin.readline().strip().split())
candy = [0] + list(map(int, sys.stdin.readline().strip().split()))
friends = {i: set() for i in range(1, N + 1)}
dp = [0] * K
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    friends[a].add(b)
    friends[b].add(a)

visited = [False] * (N + 1)
for i in range(1, N + 1):
    if visited[i]:
        continue

    q = collections.deque()
    q.append(i)
    friend = {i}
    count = candy[i]
    visited[i] = True

    while True:
        if len(q) == 0:
            break

        cur = q.popleft()

        for nxt in friends[cur]:
            if not visited[nxt]:
                q.append(nxt)
                friend.add(nxt)
                count += candy[nxt]
                visited[nxt] = True

    for j in range(K - 1, len(friend) - 1, -1):
        dp[j] = max(dp[j], dp[j - len(friend)] + count)

print(dp[-1])
