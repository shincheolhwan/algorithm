import sys
import math

directions = list(map(int, sys.stdin.readline().strip().split()))
positions = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
cost = {
    (0, 1): 2, (0, 2): 2, (0, 3): 2, (0, 4): 2, (1, 1): 1, (1, 2): 3, (1, 3): 4, (1, 4): 3, (2, 1): 3, (2, 2): 1,
    (2, 3): 3, (2, 4): 4, (3, 1): 4, (3, 2): 3, (3, 3): 1, (3, 4): 3, (4, 1): 3, (4, 2): 4, (4, 3): 3, (4, 4): 1,
}
dp = [{
    (0, 1): math.inf, (0, 2): math.inf, (0, 3): math.inf, (0, 4): math.inf, (1, 2): math.inf,
    (1, 3): math.inf, (1, 4): math.inf, (2, 3): math.inf, (2, 4): math.inf, (3, 4): math.inf,
} for _ in range(len(directions) - 1)]

for i, direction in enumerate(directions):
    if direction == 0:
        break

    if i == 0:
        dp[i][(0, direction)] = 2

    else:
        for cur_pos in positions:
            if dp[i - 1][cur_pos] == math.inf:
                continue
            else:
                cur_pos1, cur_pos2 = cur_pos
                if cur_pos1 != direction:
                    next1: tuple[int, int] = tuple(sorted([cur_pos1, direction]))
                    dp[i][next1] = min(dp[i][next1], dp[i - 1][cur_pos] + cost[(cur_pos2, direction)])

                if cur_pos2 != direction:
                    next2: tuple[int, int] = tuple(sorted([cur_pos2, direction]))
                    dp[i][next2] = min(dp[i][next2], dp[i - 1][cur_pos] + cost[(cur_pos1, direction)])

print(min(dp[-1].values()))
