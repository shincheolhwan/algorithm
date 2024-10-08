str1 = input()
str2 = input()
dp = [["" for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    c1 = str1[i - 1]
    for j in range(1, len(str2) + 1):
        c2 = str2[j - 1]
        if c1 == c2:
            dp[i][j] = dp[i - 1][j - 1] + c1
        else:
            if len(dp[i][j - 1]) > len(dp[i - 1][j]):
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

length = len(dp[len(str1)][len(str2)])
print(length)
if length != 0:
    print(dp[len(str1)][len(str2)])
