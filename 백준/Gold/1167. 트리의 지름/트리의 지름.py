import math
import sys
from queue import Queue


def dfs(start_node) -> (int, int):
    lengths = [math.inf] * (V + 1)
    lengths[0] = 0
    lengths[start_node] = 0

    q = Queue()
    q.put(start_node)

    while True:
        if q.empty():
            break

        cur_node = q.get()

        for next_node in tree[cur_node]:
            if lengths[next_node] == math.inf:
                lengths[next_node] = lengths[cur_node] + tree[cur_node][next_node]
                q.put(next_node)

    index = 0
    max_length = 0
    for i in range(len(lengths)):
        if lengths[i] >= max_length:
            index = i
            max_length = lengths[i]

    return index, max_length


V = int(sys.stdin.readline().strip())
tree = {i: {} for i in range(1, V + 1)}

for _ in range(1, V + 1):
    nums = list(map(int, sys.stdin.readline().strip().split()))
    i = nums[0]
    nums = nums[1:-1]

    for j in range(0, len(nums) - 1, 2):
        b, w = nums[j], nums[j + 1]
        tree[i][b] = w

point, _ = dfs(1)
print(dfs(point)[1])
