N = int(input())
nums = list(map(int, input().split()))

dp = [True] * (max(nums) + 1)
dp[0] = False
dp[1] = False

for i in range(2, len(dp)):
    j = 2
    while True:
        if i * j >= len(dp):
            break
        dp[i * j] = False
        j += 1

answer = 0
for num in nums:
    if dp[num]:
        answer += 1

print(answer)
