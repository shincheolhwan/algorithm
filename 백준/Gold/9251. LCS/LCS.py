str1 = list(input())
str2 = list(input())
dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    str1_c = str1[i - 1]
    for j in range(1, len(str2) + 1):
        str2_c = str2[j - 1]
        if str1_c == str2_c:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(str1)][len(str2)])
