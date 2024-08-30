N = int(input())

check = [True] * (N + 1)
check[0] = False
check[1] = False


def find_next(num):
    while True:
        num += 1
        if num > N:
            return num
        else:
            if check[num]:
                return num


for i in range(2, N):
    for j in range(2 * i, N + 1, i):
        check[j] = False

start_index = 0
end_index = 0
answer = 0
total = 0

while True:
    if start_index > end_index or end_index > N:
        break

    if total < N:
        next_prime = find_next(end_index)
        if next_prime > N:
            break
        else:
            total += next_prime
            end_index = next_prime
    elif total == N:
        answer += 1
        next_prime = find_next(end_index)
        if next_prime > N:
            break
        else:
            total += next_prime
            end_index = next_prime
    else:
        next_prime = find_next(start_index)
        if next_prime > N:
            break
        else:
            total -= next_prime
            start_index = next_prime
print(answer)
