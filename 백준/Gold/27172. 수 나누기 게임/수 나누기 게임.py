N = int(input())
cards = list(map(int, input().split()))
max_card = max(cards)
check = set(cards)
answer = [0] * 1_000_001

for i in cards:
    for num in range(2 * i, max_card + 1, i):
        if num in check:
            answer[i] += 1
            answer[num] -= 1

for num in cards:
    print(answer[num], end=" ")
