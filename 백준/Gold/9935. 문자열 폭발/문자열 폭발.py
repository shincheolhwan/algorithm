import sys

string = list(sys.stdin.readline().strip())
bomb = list(sys.stdin.readline().strip())
answer = []

for i in range(len(string)):
    c = string[i]
    answer.append(c)

    if c == bomb[-1] and len(answer) >= len(bomb):
        is_same = True
        for j in range(len(bomb)):
            if answer[-j - 1] != bomb[-j - 1]:
                is_same = False
                break

        if is_same:
            for _ in range(len(bomb)):
                answer.pop()

if len(answer) == 0:
    print("FRULA")
else:
    print("".join(answer))
