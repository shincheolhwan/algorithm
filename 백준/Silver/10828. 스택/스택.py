import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0

    def top(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[-1]


N = int(sys.stdin.readline())
stack = Stack()

for _ in range(N):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())
    elif command[0] == 'top':
        print(stack.top())
    else:
        print('Invalid command')
