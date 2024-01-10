from collections import defaultdict


def solution(L):
    MAX = 10**6
    D = defaultdict(set)
    for x in range(1, MAX):
        for y in range(x, MAX, x):
            D[y].add(x)

    ans = 0
    for i, x in enumerate(L):
        left = sum(y in D[x] for y in L[:i])
        right = sum(x in D[y] for y in L[i + 1 :])
        ans += left * right

    return ans
