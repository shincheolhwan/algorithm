import sys

sys.setrecursionlimit(10 ** 9)


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        union_find[max(x, y)] = min(x, y)


def find(x):
    if union_find[x] != x:
        union_find[x] = find(union_find[x])
    return union_find[x]


N, M = map(int, sys.stdin.readline().strip().split())

union_find = [i for i in range(0, N + 1)]
known = set(list(map(int, sys.stdin.readline().strip().split()))[1:])
parties = []

for _ in range(M):
    party = set(list(map(int, sys.stdin.readline().strip().split()))[1:])
    parties.append(party)
    parent = min(party)
    for child in party:
        union(parent, child)

union_known = set()
for k in known:
    union_known.add(find(k))

answer = len(parties)
for party in parties:
    for participant in party:
        if find(participant) in union_known:
            answer -= 1
            break
print(answer)
