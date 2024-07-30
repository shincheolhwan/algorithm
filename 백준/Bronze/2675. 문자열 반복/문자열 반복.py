T = int(input())
for _ in range(T):
    R, S = input().split()
    answer = ""
    for c in list(S):
        answer += c * int(R)
    print(answer)
