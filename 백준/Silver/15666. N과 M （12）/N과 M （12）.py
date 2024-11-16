import itertools

N, M = map(int, input().split())
A = sorted(list(set(list(map(int, input().split())))))

for combi in itertools.combinations_with_replacement(A, M):
    print(*combi)
