import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

counter = {}
for num in nums:
    counter[num] = counter.get(num, 0) + 1

M = sys.stdin.readline()
checks = list(map(int, sys.stdin.readline().split()))

for check in checks:
    print(counter.get(check, 0), end=" ")
