A, B, C = map(int, input().split())


def remain(a, b, c):
    if b == 1:
        return a % c

    next_b = b // 2
    temp = remain(a, next_b, c)

    if b % 2 == 0:
        return (temp * temp) % c
    else:
        return (temp * temp * a) % c


print(remain(A, B, C))
