import sys

N = int(sys.stdin.readline().strip())
times = list(map(int, sys.stdin.readline().strip().split()))
times.sort()

answer = 0
acc = 0
for time in times:
    acc += time
    answer += acc

print(answer)
