import sys

sys.setrecursionlimit(10 ** 9)


def recursion(tree):
    if len(tree) == 0:
        return

    root = tree[0]
    left = tree[1:]
    right = []
    for i in range(1, len(tree)):
        if tree[i] > root:
            left = tree[1:i]
            right = tree[i:]
            break

    recursion(left)
    recursion(right)
    print(root)


nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break

recursion(nums)
