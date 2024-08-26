import sys
import math

N = int(sys.stdin.readline().strip())
solutions = list(map(int, sys.stdin.readline().strip().split()))

sol1, sol2 = 0, 0
diff = math.inf

for i, solution in enumerate(solutions):
    start = i + 1
    end = N - 1

    while True:
        if start > end:
            break

        mid = (start + end) // 2
        temp = solution + solutions[mid]

        if abs(temp) < diff:
            diff = abs(temp)
            sol1 = solution
            sol2 = solutions[mid]

        if temp < 0:
            start = mid + 1
        else:
            end = mid - 1

print(f"{sol1} {sol2}")
