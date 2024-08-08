import sys


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order(r):
    if r is None:
        return

    print(r.val, end="")
    pre_order(r.left)
    pre_order(r.right)


def in_order(r):
    if r is None:
        return

    in_order(r.left)
    print(r.val, end="")
    in_order(r.right)


def post_order(r):
    if r is None:
        return

    post_order(r.left)
    post_order(r.right)
    print(r.val, end="")


N = int(sys.stdin.readline().strip())

nodes = {}
for i in range(N):
    parent, left_child, right_child = sys.stdin.readline().strip().split()
    if parent not in nodes:
        nodes[parent] = Node(parent)
    if left_child not in nodes and left_child != ".":
        nodes[left_child] = Node(left_child)
    if right_child not in nodes and right_child != ".":
        nodes[right_child] = Node(right_child)

    nodes[parent].left = nodes.get(left_child, None)
    nodes[parent].right = nodes.get(right_child, None)

root = nodes["A"]
pre_order(root)
print()
in_order(root)
print()
post_order(root)
