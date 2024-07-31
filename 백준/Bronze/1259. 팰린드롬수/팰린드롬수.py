while True:
    s = input()

    if s == "0":
        break

    answer = "yes"
    for i in range(len(s) // 2):

        # print(i)
        # print(len(s) - 1 - i)
        # print(s[i])
        # print(s[len(s) - 1 - i])

        if s[i] != s[len(s) - 1 - i]:
            answer = "no"
            break

    print(answer)
