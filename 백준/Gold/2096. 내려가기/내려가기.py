import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
dp_min = nums.copy()
dp_max = nums.copy()

for i in range(1, N):
    nums = list(map(int, sys.stdin.readline().strip().split()))
    before_dp_min = dp_min.copy()
    before_dp_max = dp_max.copy()
    for j in range(3):
        cur = nums[j]
        if j == 0:
            dp_min[j] = min(before_dp_min[0] + cur, before_dp_min[1] + cur)
            dp_max[j] = max(before_dp_max[0] + cur, before_dp_max[1] + cur)
        elif j == 1:
            dp_min[j] = min(before_dp_min[0] + cur, before_dp_min[1] + cur, before_dp_min[2] + cur)
            dp_max[j] = max(before_dp_max[0] + cur, before_dp_max[1] + cur, before_dp_max[2] + cur)
            pass
        elif j == 2:
            dp_min[j] = min(before_dp_min[1] + cur, before_dp_min[2] + cur)
            dp_max[j] = max(before_dp_max[1] + cur, before_dp_max[2] + cur)

print(f"{max(dp_max)} {min(dp_min)}")
