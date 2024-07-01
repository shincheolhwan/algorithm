import itertools


def solution(dice):
    combination = combi(dice)
    answer = getAnswer(len(dice), combination)
    return answer


def combi(dice):
    n = len(dice)
    total = list(range(0, n))
    combination = list(itertools.combinations(total, n // 2))
    dict_dice = diceToDict(dice)

    result = {}
    for comb in combination:
        sums = {}
        for num in comb:
            sums = getSums(sums, dict_dice[num])
        result[comb] = sums

    return result


def diceToDict(dice):
    result = []
    n = len(dice)
    for i in range(n):
        cur = {}
        for num in dice[i]:
            if cur.get(num) is None:
                cur[num] = 1
            else:
                cur[num] += 1
        result.append(cur)
    return result


def getSums(dict1, dict2):
    result = {}
    if len(dict1.keys()) == 0:
        return dict2
    if len(dict2.keys()) == 0:
        return dict2

    for num1 in dict1.keys():
        for num2 in dict2.keys():
            if result.get(num1 + num2) is None:
                result[num1 + num2] = dict1[num1] * dict2[num2]
            else:
                result[num1 + num2] += dict1[num1] * dict2[num2]
    return result


def getAnswer(n, combination):
    total = set(range(0, n))
    max_win_count = 0
    max_win_combination = None
    done = set()

    for comb in combination:
        if comb in done:
            continue

        a = comb
        b = tuple(total.difference(comb))
        comb_a = combination.get(a)
        comb_b = combination.get(b)

        win_count, draw_count, lose_count = compare(comb_a, comb_b)

        if win_count > max_win_count:
            max_win_count = win_count
            max_win_combination = a

        if lose_count > max_win_count:
            max_win_count = lose_count
            max_win_combination = b

        done.add(a)
        done.add(b)

    answer = []
    for num in max_win_combination:
        answer.append(num + 1)

    print(f"max_win_count: {max_win_count}")
    print(f"max_win_combination: {answer}")

    return answer


def compare(dict1, dict2):
    win_count = 0
    draw_count = 0
    lose_count = 0

    for key1 in dict1:
        for key2 in dict2:
            if key1 > key2:
                win_count += dict1[key1] * dict2[key2]
            elif key1 == key2:
                draw_count += dict1[key1] * dict2[key2]
            elif key1 < key2:
                lose_count += dict1[key1] * dict2[key2]
            else:
                print("error")

    return win_count, draw_count, lose_count
