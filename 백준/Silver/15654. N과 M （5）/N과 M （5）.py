N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
permutations = []


def dfs(cur):
    if len(cur) == M:
        permutations.append(tuple(cur))
        return

    for num in nums:
        if num in cur:
            continue
        else:
            cur.append(num)
            dfs(cur)
            cur.pop()


dfs([])
for permutation in permutations:
    print(*permutation)
