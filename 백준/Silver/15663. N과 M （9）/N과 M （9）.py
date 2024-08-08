N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

seqs = []
visited = set()


def dfs(cur):
    if len(cur) == M:
        seqs.append(tuple(cur))
        return

    for i in range(N):
        if i in visited:
            continue

        if i > 0 and i - 1 not in visited and A[i - 1] == A[i]:
            continue

        cur.append(A[i])
        visited.add(i)
        dfs(cur)
        cur.pop()
        visited.remove(i)


dfs([])
for seq in seqs:
    print(*seq)
