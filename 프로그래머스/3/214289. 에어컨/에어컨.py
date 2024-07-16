MAX_POWER = 1000 * 100


def solution(temperature, t1, t2, a, b, onboard):
    return dynamic_programming(temperature, t1, t2, a, b, onboard)


def dynamic_programming(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10
    dp = [[MAX_POWER] * 51 for _ in range(len(onboard))]
    dp[0][temperature] = 0

    for i in range(0, len(onboard) - 1):
        is_onboard = onboard[i + 1]
        for j in range(51):
            if dp[i][j] == MAX_POWER:
                continue
            # print(f"time: {i}, temp: {j}, dp[{i}][{j}] = {dp[i][j]}")

            # off
            if j < temperature:
                next_temp = j + 1
            elif j == temperature:
                next_temp = j
            else:
                next_temp = j - 1

            if is_onboard == 1 and t1 <= next_temp <= t2:
                dp[i + 1][next_temp] = min(dp[i + 1][next_temp], dp[i][j])
            elif is_onboard == 0 and 0 <= next_temp <= 50:
                dp[i + 1][next_temp] = min(dp[i + 1][next_temp], dp[i][j])

            # on(희망 온도와 같은 경우)
            next_temp = j
            if is_onboard == 1 and t1 <= next_temp <= t2:
                dp[i + 1][next_temp] = min(dp[i + 1][next_temp], dp[i][j] + b)
            elif is_onboard == 0 and 0 <= next_temp <= 50:
                dp[i + 1][next_temp] = min(dp[i + 1][next_temp], dp[i][j] + b)

            # on(희망온도보다 높은 경우)
            next_temp = j - 1
            if is_onboard == 1 and t1 <= next_temp <= t2:
                dp[i + 1][next_temp] = min(dp[i + 1][next_temp], dp[i][j] + a)
            elif is_onboard == 0 and 0 <= next_temp <= 50:
                dp[i + 1][next_temp] = min(dp[i + 1][next_temp], dp[i][j] + a)

            # on(희망온도보다 낮은 경우)
            next_temp = j + 1
            if is_onboard == 1 and t1 <= next_temp <= t2:
                dp[i + 1][next_temp] = min(dp[i + 1][next_temp], dp[i][j] + a)
            elif is_onboard == 0 and 0 <= next_temp <= 50:
                dp[i + 1][next_temp] = min(dp[i + 1][next_temp], dp[i][j] + a)
    return min(dp[len(onboard) - 1])


# print(solution(28, 17, 26, 10, 8, [0, 0, 1, 1, 1, 1, 1]), 40)
# print(solution(-10, -5, 5, 5, 1, [0, 0, 0, 0, 0, 1, 0]), 25)
# print(solution(11, 8, 10, 10, 1, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]), 20)
# print(solution(11, 8, 10, 10, 100, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]), 60)
