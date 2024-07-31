from queue import Queue

N = int(input())

count = 0
if N != 1:
    q = Queue()
    checks = {N}
    q.put(N)
    next_cur = -1

    while True:
        count += 1
        for _ in range(q.qsize()):
            cur = q.get()

            if cur % 3 == 0:
                next_cur = cur // 3
                if next_cur == 1:
                    break
                if next_cur not in checks:
                    checks.add(next_cur)
                    q.put(next_cur)
            if cur % 2 == 0:
                next_cur = cur // 2
                if next_cur == 1:
                    break
                if next_cur not in checks:
                    checks.add(next_cur)
                    q.put(next_cur)

            next_cur = cur - 1
            if next_cur == 1:
                break
            if next_cur not in checks:
                checks.add(next_cur)
                q.put(next_cur)

        if next_cur == 1:
            break

print(count)
