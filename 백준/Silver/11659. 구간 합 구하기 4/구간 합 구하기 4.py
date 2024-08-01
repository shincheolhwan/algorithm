import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
sums = [0]
for i in range(len(nums)):
    sums.append(nums[i] + sums[i])


for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    print(sums[end] - sums[start - 1])
