import sys

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().strip().split()))

sum1 = {}
sum2 = {}

for i in range(n):
    total = 0
    for j in range(i, n):
        total += A[j]
        sum1[total] = sum1.get(total, 0) + 1

for i in range(m):
    total = 0
    for j in range(i, m):
        total += B[j]
        sum2[total] = sum2.get(total, 0) + 1

answer = 0
for num1 in sum1:
    if T - num1 in sum2:
        answer += sum1[num1] * sum2[T - num1]

print(answer)