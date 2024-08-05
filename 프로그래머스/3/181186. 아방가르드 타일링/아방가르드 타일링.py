def solution(n):
    mod = 1_000_000_007

    memo = [12, 2, 4]
    dp = [0] * (max(n, 3) + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    dp[3] = 10

    for i in range(4, n + 1):
        temp = memo[i % 3]
        temp += dp[i - 1] + dp[i - 2] * 2 + dp[i - 3] * 5
        dp[i] = temp

        memo[i % 3] += dp[i - 1] * 2 + dp[i - 2] * 2 + dp[i - 3] * 4

    return dp[n] % mod
