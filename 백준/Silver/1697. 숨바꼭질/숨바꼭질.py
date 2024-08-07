from queue import Queue

N, K = map(int, input().split())

q = Queue()
q.put(N)
visited = {N}
time_count = 0
answer = 100_000
find = N == K

while True:
    if q.empty() or find or time_count >= answer:
        break

    for _ in range(q.qsize()):
        cur = q.get()
        next_positions = [cur + 1, cur - 1, cur * 2]
        if K in next_positions:
            find = True
            break

        for next_position in next_positions:
            if next_position not in visited:
                visited.add(next_position)
                if next_position > K:
                    answer = min(answer, time_count + 1 + next_position - K)
                else:
                    q.put(next_position)

    time_count += 1

if find:
    print(min(time_count, answer))
else:
    print(answer)
