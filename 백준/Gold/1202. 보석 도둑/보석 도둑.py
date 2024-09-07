import sys
import heapq

N, K = map(int, sys.stdin.readline().strip().split())

jewel = []

for _ in range(N):
    M, V = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(jewel, (M, V))

bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))

bags.sort()

answer = 0
values = []
for bag in bags:
    while True:
        if not jewel or jewel[0][0] > bag:
            break
        _, V = heapq.heappop(jewel)
        heapq.heappush(values, -V)

    if values:
        answer -= heapq.heappop(values)

print(answer)
