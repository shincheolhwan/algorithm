import itertools

N, M = map(int, input().split())
A = list(range(1, N + 1))

for combi in itertools.combinations_with_replacement(A, M):
    print(*combi)
