import sys
import math

sys.setrecursionlimit(10 ** 9)


def get_count(n):
    if n <= 0:
        return 0

    power = int(math.log2(n))

    if 2 ** power == n:
        return nums[power] + 1
    else:
        return nums[power] + (n + 1 - 2 ** power) + get_count(n - 2 ** power)


A, B = map(int, sys.stdin.readline().strip().split())
nums = [0]
for i in range(int(math.log2(B)) + 1):
    nums.append(2 ** i + 2 * nums[i])
print(get_count(B) - get_count(A - 1))
