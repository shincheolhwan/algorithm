import sys


class Set:
    def __init__(self):
        self.items = set()

    def add(self, x):
        self.items.add(x)

    def remove(self, x):
        if x in self.items:
            self.items.remove(x)

    def check(self, x):
        if x in self.items:
            return 1
        else:
            return 0

    def toggle(self, x):
        if x in self.items:
            self.remove(x)
        else:
            self.add(x)

    def all(self):
        self.items = {i for i in range(1, 21)}

    def empty(self):
        self.items = set()


N = int(sys.stdin.readline().strip())
my_set = Set()

for _ in range(N):
    command = sys.stdin.readline().strip().split()

    if command[0] == "add":
        my_set.add(int(command[1]))
    elif command[0] == "remove":
        my_set.remove(int(command[1]))
    elif command[0] == "check":
        print(my_set.check(int(command[1])))
    elif command[0] == "toggle":
        my_set.toggle(int(command[1]))
    elif command[0] == "all":
        my_set.all()
    elif command[0] == "empty":
        my_set.empty()
