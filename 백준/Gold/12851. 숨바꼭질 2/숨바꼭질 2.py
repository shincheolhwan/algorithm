import heapq
import math

N, K = map(int, input().split())

if N == K:
    print(0)
    print(1)
    exit(0)

pq = [(0, N)]
dp = [math.inf] * 200_001
dp[N] = 0

find_time = math.inf
method = 0

while pq:
    cur_time, cur_pos = heapq.heappop(pq)
    if cur_time >= find_time:
        break

    next_pos = cur_pos - 1
    if 0 <= next_pos <= 200_000:
        if next_pos == K:
            find_time = cur_time + 1
            method += 1
        elif dp[next_pos] >= cur_time + 1:
            dp[next_pos] = cur_time + 1
            heapq.heappush(pq, (cur_time + 1, next_pos))

    next_pos = cur_pos + 1
    if 0 <= next_pos <= 200_000:
        if next_pos == K:
            find_time = cur_time + 1
            method += 1
        elif dp[next_pos] >= cur_time + 1:
            dp[next_pos] = cur_time + 1
            heapq.heappush(pq, (cur_time + 1, next_pos))

    next_pos = 2 * cur_pos
    if 0 <= next_pos <= 200_000:
        if next_pos == K:
            find_time = cur_time + 1
            method += 1
        elif dp[next_pos] >= cur_time + 1:
            dp[next_pos] = cur_time + 1
            heapq.heappush(pq, (cur_time + 1, next_pos))

print(find_time)
print(method)
