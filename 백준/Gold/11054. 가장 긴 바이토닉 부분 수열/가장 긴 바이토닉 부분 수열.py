import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))

dp1 = [1] * N
dp2 = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

    reverse_i = N - 1 - i
    for j in range(N - 1, reverse_i - 1, -1):
        if A[reverse_i] > A[j]:
            dp2[reverse_i] = max(dp2[reverse_i], dp2[j] + 1)

answer = 0
for i in range(N):
    answer = max(answer, dp1[i] + dp2[i] - 1)
print(answer)
