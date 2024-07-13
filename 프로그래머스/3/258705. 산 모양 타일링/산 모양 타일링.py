def solution(n, tops):
    a = [0 for _ in range(n + 1)]
    b = [0 for _ in range(n + 1)]
    a[0] = 0
    b[0] = 1

    for i in range(len(tops)):
        if tops[i] == 1:
            a[i + 1] = a[i] + b[i]
            b[i + 1] = 2 * a[i] + 3 * b[i]
        else:
            a[i + 1] = a[i] + b[i]
            b[i + 1] = a[i] + 2 * b[i]

    return (a[n] + b[n]) % 10007

