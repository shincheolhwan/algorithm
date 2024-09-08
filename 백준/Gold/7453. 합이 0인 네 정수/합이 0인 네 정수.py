import sys

n = int(sys.stdin.readline())
A = []
B = []
C = []
D = []
sum_AB = {}

for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().strip().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for i in range(n):
    for j in range(n):
        sum_AB[A[i] + B[j]] = sum_AB.get(A[i] + B[j], 0) + 1

answer = 0
for i in range(n):
    for j in range(n):
        if -C[i] - D[j] in sum_AB:
            answer += sum_AB[-C[i] - D[j]]

print(answer)