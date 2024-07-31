import sys

N = int(sys.stdin.readline())

points = []
for _ in range(N):
    x, y = sys.stdin.readline().split()
    points.append((int(x), int(y)))

points.sort(key=lambda p: (p[0], p[1]))

for x, y in points:
    print(f"{x} {y}")
