from queue import Queue

A, B = map(int, input().split())

if A == B:
    print(1)
    exit()

q = Queue()
q.put(A)

dp = {A}

answer = -1
count = 2
while True:
    if q.empty() or answer != -1:
        break

    for _ in range(q.qsize()):
        cur = q.get()

        nxt = cur * 2
        if nxt not in dp:
            dp.add(nxt)
            if nxt == B:
                answer = count
                break
            elif nxt < B:
                q.put(nxt)

        nxt = cur * 10 + 1
        if nxt not in dp:
            dp.add(nxt)
            if nxt == B:
                answer = count
                break
            elif nxt < B:
                q.put(nxt)
    count += 1

print(answer)
