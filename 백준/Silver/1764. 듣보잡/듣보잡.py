import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

a = set()
b = set()

for _ in range(N):
    a.add(sys.stdin.readline().rstrip())

for _ in range(M):
    b.add(sys.stdin.readline().rstrip())

answer = list(a.intersection(b))
answer.sort()

print(len(answer))
for person in answer:
    print(person)
    
