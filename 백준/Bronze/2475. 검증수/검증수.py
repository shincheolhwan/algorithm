nums = map(int, input().split())
answer = 0

for num in nums:
    answer += num ** 2

print(answer % 10)
