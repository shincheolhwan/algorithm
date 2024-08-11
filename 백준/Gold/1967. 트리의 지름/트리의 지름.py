import sys

sys.setrecursionlimit(10 ** 9)


class Node:
    def __init__(self, value):
        self.value = value
        self.distance = 0
        self.children = []

    def set_distance(self, distance):
        self.distance = distance

    def add_child(self, child):
        self.children.append(child)


def get_diameter(node: Node) -> (int, int):
    max_diameter = 0
    radius = []
    for child in node.children:
        diameter, max_radius = get_diameter(child)
        max_diameter = max(max_diameter, diameter)
        radius.append(max_radius)
    radius.sort(reverse=True)

    if len(radius) >= 2:
        return max(radius[0] + radius[1], radius[0] + node.distance, max_diameter), radius[0] + node.distance
    elif len(radius) == 1:
        return max(radius[0] + node.distance, max_diameter), radius[0] + node.distance
    else:
        return node.distance, node.distance


n = int(sys.stdin.readline().strip())
nodes = [Node(i) for i in range(n + 1)]
for _ in range(n - 1):
    p, c, w = map(int, sys.stdin.readline().strip().split())
    nodes[p].add_child(nodes[c])
    nodes[c].set_distance(w)

print(get_diameter(nodes[1])[0])
