import sys

mod = 1000000007


def gcd(a, b):
    a, b = max(a, b), min(a, b)

    while True:
        if b == 0:
            break
        tmp = a % b
        a = b
        b = tmp

    return a


def getExp(num, exp):
    if exp == 1:
        return num % mod

    if exp % 2 == 0:
        half = getExp(num, exp // 2)
        return (half * half) % mod
    else:
        return (num * getExp(num, exp - 1)) % mod


M = int(sys.stdin.readline().strip())
answer = 0
for _ in range(M):
    N, S = map(int, sys.stdin.readline().strip().split())
    divider = gcd(N, S)
    N //= divider
    S //= divider
    answer += (S * getExp(N, mod - 2)) % mod
    answer %= mod

print(answer)
