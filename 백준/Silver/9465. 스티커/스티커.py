import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    scores = []
    dp = []
    for _ in range(2):
        scores.append(list(map(int, sys.stdin.readline().strip().split())))
        dp.append([0] * n)

    dp[0][0] = scores[0][0]
    dp[1][0] = scores[1][0]

    if n >= 2:
        dp[0][1] = dp[1][0] + scores[0][1]
        dp[1][1] = dp[0][0] + scores[1][1]

    for i in range(2, n):
        for j in range(2):
            if j == 0:
                dp[0][i] = max(dp[0][i], dp[0][i - 2] + scores[0][i])
                dp[0][i] = max(dp[0][i], dp[1][i - 2] + scores[0][i])
                dp[0][i] = max(dp[0][i], dp[1][i - 1] + scores[0][i])
            else:
                dp[1][i] = max(dp[1][i], dp[1][i - 2] + scores[1][i])
                dp[1][i] = max(dp[1][i], dp[0][i - 2] + scores[1][i])
                dp[1][i] = max(dp[1][i], dp[0][i - 1] + scores[1][i])

    print(max(max(dp[0]), max(dp[1])))
