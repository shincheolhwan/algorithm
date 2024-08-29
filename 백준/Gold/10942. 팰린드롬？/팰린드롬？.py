import sys


def isPalindrome():
    dp = [[0] * N for _ in range(N)]

    for count in range(N):
        for i in range(N - count):
            j = i + count
            if i == j:
                dp[i][j] = 1
            else:
                if nums[i] == nums[j]:
                    if count == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

    return dp


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
dp = isPalindrome()

M = int(sys.stdin.readline())
for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    print(dp[start - 1][end - 1])

