import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))
trees.sort(reverse=True)

start, end = 1, max(trees)

while True:
    if start > end:
        break

    mid = (start + end) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
        else:
            break

    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
