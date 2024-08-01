import sys


class Heap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        self.heap.append(x)
        cur_i = len(self.heap) - 1
        while True:
            if cur_i == 0:
                break

            next_i = (cur_i - 1) // 2
            if self.heap[cur_i] >= self.heap[next_i]:
                break
            else:
                self.heap[cur_i], self.heap[next_i] = self.heap[next_i], self.heap[cur_i]
                cur_i = next_i

    def pop(self):
        if len(self.heap) == 0:
            return 0

        else:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            value = self.heap.pop()

            cur = 0
            while True:
                left = cur * 2 + 1
                right = cur * 2 + 2
                min_index = cur

                if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
                    min_index = left

                if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
                    min_index = right

                if min_index == cur:
                    break
                else:
                    self.heap[min_index], self.heap[cur] = self.heap[cur], self.heap[min_index]
                    cur = min_index

            return value


h = Heap()
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    command = int(sys.stdin.readline().rstrip())

    if command == 0:
        print(h.pop())
    else:
        h.push(command)
