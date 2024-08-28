import math

N, S = map(int, input().split())
nums = list(map(int, input().split()))

start_index = 0
end_index = 0
sums = 0
min_length = math.inf

while True:
    if end_index >= N:
        break

    sums += nums[end_index]

    if sums >= S:
        min_length = min(min_length, end_index - start_index + 1)

        while True:
            sums -= nums[start_index]
            start_index += 1
            if sums >= S:
                min_length = min(min_length, end_index - start_index + 1)
            else:
                break

            if start_index == end_index:
                break

    end_index += 1

if min_length == math.inf:
    print(0)
else:
    print(min_length)
