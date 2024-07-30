max_i = 0
max_num = -1

for i in range(1, 10):
    num = int(input())
    if num > max_num:
        max_num = num
        max_i = i

print(max_num)
print(max_i)
