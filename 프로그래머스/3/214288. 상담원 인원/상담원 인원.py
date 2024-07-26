from queue import PriorityQueue, Queue
import math


def solution(k, n, reqs):
    requests = split_reqs(k, reqs)
    # print(f"split: {requests}")

    wait_times = []
    for k_reqs in requests:
        wait_times_per_mento = get_wait_time(n - k + 1, k_reqs)
        wait_times.append(wait_times_per_mento)

    # print(f"wait_times: {wait_times}")

    return get_min(n - k + 1, n, wait_times)


def split_reqs(k, reqs):
    result = [[] for _ in range(k)]

    for req in reqs:
        result[req[2] - 1].append(req[:2])

    return result


def get_wait_time(max_mento, reqs):
    result = [-1] * (max_mento + 1)

    for i in range(1, max_mento + 1):
        pq = PriorityQueue()
        wait_time = 0
        for req in reqs:
            if pq.qsize() < i:
                pq.put(req[0] + req[1])
            else:
                finish_time = pq.get()
                if finish_time > req[0]:
                    wait_time += finish_time - req[0]
                    pq.put(finish_time + req[1])
                else:
                    pq.put(req[0] + req[1])
        else:
            result[i] = wait_time

    return result


def get_min(max_mento, n, wait_times):
    q = Queue()
    for _ in range(len(wait_times)):
        if q.qsize() == 0:
            for i in range(1, max_mento + 1):
                q.put([i])
        else:
            for _ in range(q.qsize()):
                cur = q.get()

                for i in range(1, max_mento + 1):
                    q.put(cur + [i])

    min_wait = math.inf
    for _ in range(q.qsize()):
        cur = q.get()

        if sum(cur) > n:
            continue
        wait_time = 0
        for i, mento in enumerate(cur):
            wait_time += wait_times[i][mento]

        min_wait = min(min_wait, wait_time)

    return min_wait


# print(solution(3, 5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]), 25)
# print(solution(2, 3, [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]), 90)
