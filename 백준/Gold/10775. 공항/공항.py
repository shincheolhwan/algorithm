import sys

sys.setrecursionlimit(10 ** 6)


def set_count(x: int) -> int:
    if x <= 0:
        return -1
    if x == gates[x]:
        gates[x] -= 1
        return gates[x]
    else:
        gates[x] = set_count(gates[x])
        return gates[x]


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
gates = [i for i in range(0, G + 1)]
gates[0] = -1

answer = 0
for _ in range(P):
    g = int(sys.stdin.readline())
    result = set_count(g)
    if result == -1:
        break
    else:
        answer += 1
print(answer)
