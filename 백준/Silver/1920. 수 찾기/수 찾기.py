import sys

N = int(sys.stdin.readline())
nums = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

for check in checks:
    if check in nums:
        print(1)
    else:
        print(0)
