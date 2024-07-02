# 2024.07.24 16:54 시작
from queue import PriorityQueue


def solution(coin, cards):
    answer = 1
    n = len(cards)
    card_index = len(cards) // 3
    start_cards = set(cards[:card_index])
    cur_cards = set(cards[:card_index])
    discard_cards = makeInitialDiscardCards(len(cards), start_cards)
    # print(f"discard_cards: {discard_cards.queue}")

    while True:
        # print(f"answer: {answer}, card_index: {card_index}, coin: {coin}")
        if card_index + 1 >= len(cards):
            break

        cur_num = cards[card_index]
        pair_num = n + 1 - cur_num
        cur_cards.add(cur_num)
        if pair_num in cur_cards:
            if pair_num in start_cards:
                discard_cards.put((1, cur_num, pair_num))
            else:
                discard_cards.put((2, cur_num, pair_num))

        cur_num = cards[card_index + 1]
        pair_num = n + 1 - cur_num
        cur_cards.add(cur_num)
        if pair_num in cur_cards:
            if pair_num in start_cards:
                discard_cards.put((1, cur_num, pair_num))
            else:
                discard_cards.put((2, cur_num, pair_num))

        card_index += 2
        # print(f"discard_cards: {discard_cards.queue}")
        if discard_cards.qsize() == 0:
            break

        use_coin, card1, card2 = discard_cards.get()
        if use_coin == 0 or use_coin < coin:
            answer += 1
            coin -= use_coin
            cur_cards.discard(card1)
            cur_cards.discard(card2)
        elif use_coin == coin:
            answer += 1
            coin = 0
            cur_cards.discard(card1)
            cur_cards.discard(card2)
            break
        else:
            break

    return answer


def makeInitialDiscardCards(n, cards):
    result = PriorityQueue()
    pairs = set()

    for card in cards:
        pair_card = n + 1 - card
        if pair_card in cards:
            if card < pair_card:
                pair = (0, card, pair_card)
            else:
                pair = (0, pair_card, card)
            pairs.add(pair)

    for pair in pairs:
        result.put(pair)

    return result


# print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))
# print(solution(3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]))
# print(solution(2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]))
# print(solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
# print(solution(0, [12, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]))
