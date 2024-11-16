import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().strip().split()))

common = set(A) & set(B)

answer = []
while True:
    if len(common) == 0:
        break

    max_value = max(common)
    answer.append(max_value)

    A = A[A.index(max_value) + 1:]
    B = B[B.index(max_value) + 1:]
    common = set(A) & set(B)

print(len(answer))
print(*answer)
