import sys
import math
import itertools

N, M = map(int, sys.stdin.readline().strip().split())
home = []
chicken = []

for i in range(N):
    city = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(N):
        if city[j] == 1:
            home.append((i, j))
            pass
        elif city[j] == 2:
            chicken.append((i, j))
            pass

dist = [[] for i in range(len(home))]

for i in range(len(home)):
    home_x, home_y = home[i]
    for chic_x, chic_y in chicken:
        dist[i].append(abs(home_x - chic_x) + abs(home_y - chic_y))

answer = math.inf
for combi in list(itertools.combinations([i for i in range(len(chicken))], M)):
    chicken_distance = 0

    for distance in dist:
        min_distance = math.inf
        for selected in combi:
            min_distance = min(min_distance, distance[selected])
        chicken_distance += min_distance

    answer = min(answer, chicken_distance)

print(answer)
