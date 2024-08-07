import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

sorted_nums = sorted(nums)

counter = {}
count = 0
for num in sorted_nums:
    if num not in counter:
        counter[num] = count
        count += 1

for num in nums:
    print(f"{counter[num]}", end=" ")
