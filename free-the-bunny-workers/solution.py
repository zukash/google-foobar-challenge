from itertools import combinations
from functools import reduce
from operator import or_


def distribute(n, m):
    """
    Distribute keys to n people, m keys each
    """
    res = [[] for _ in range(n)]
    # Enumerate all combinations of m people receiving a particular key
    for key, I in enumerate(combinations(range(n), m)):
        for i in I:
            res[i].append(key)
    return res


def check(DD, n, k):
    """
    Check if the distribution DD satisfies the conditions of the problem
    """
    DD = [set(D) for D in DD]
    all_keys = reduce(or_, DD)
    ok = True
    for I in combinations(range(n), k):
        ok &= reduce(or_, [DD[i] for i in I]) == all_keys
    return ok


def solution(n, k):
    for m in range(1, n + 1):
        DD = distribute(n, m)
        if check(DD, n, k):
            return DD
