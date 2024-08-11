from queue import PriorityQueue

N, K = map(int, input().split())


def bfs(n, k):
    if n == k:
        return 0
    answer = 100_000
    visited = set()
    visited.add(n)
    pq = PriorityQueue()
    pq.put((0, n))

    while True:
        if pq.empty():
            break

        time, pos = pq.get()
        if time >= answer:
            break

        next_pos = pos * 2
        if next_pos == k:
            answer = min(answer, time)
        elif next_pos not in visited and 0 <= next_pos < k:
            pq.put((time, next_pos))
            visited.add(next_pos)
        elif next_pos not in visited and next_pos > k:
            answer = min(answer, time + (next_pos - k))

        next_pos = pos + 1
        if next_pos == k:
            answer = min(answer, time + 1)
        elif next_pos not in visited and 0 <= next_pos < k:
            pq.put((time + 1, next_pos))
            visited.add(next_pos)

        next_pos = pos - 1
        if next_pos == k:
            answer = min(answer, time + 1)
        elif next_pos not in visited and 0 <= next_pos <= 100_000:
            pq.put((time + 1, next_pos))
            visited.add(next_pos)

    return answer


print(bfs(N, K))
