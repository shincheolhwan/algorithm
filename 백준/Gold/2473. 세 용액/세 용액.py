import sys
import math

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
A.sort()
answer = []
answer_sum = math.inf

for i in range(N - 2):
    start = i + 1
    end = N - 1

    while True:
        if start >= end:
            break

        cur_sum = A[i] + A[start] + A[end]

        if abs(cur_sum) < abs(answer_sum):
            answer_sum = cur_sum
            answer = [A[i], A[start], A[end]]

        if cur_sum < 0:
            start += 1
        else:
            end -= 1

print(*answer)
