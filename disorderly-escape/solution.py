# coding: utf-8
from math import factorial
from collections import defaultdict


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


# Notation:
#  term: ((e0, e1), v) → v * x0^e0 * x1^e1
#  polynomial: [((e0, e1), v), ...] → Σ v * x0^e0 * x1^e1


def cycle_index(n):
    """
    Cycle index of the symmetric group S(n)
    """
    # Enumerating terms that satisfy Σ i * ei == n
    Q = [((0,), 0)]
    for i in range(1, n + 1):
        nQ = []
        for e in range(n + 1):
            for T, c in Q:
                if c + i * e <= n:
                    nQ.append((T + (e,), c + i * e))
        Q = nQ

    # Calculating the cycle index
    # ref. https://oeis.org/A181897
    PP = []
    for T, c in Q:
        if c != n:
            continue
        v = factorial(n)
        for i, e in enumerate(T):
            v //= factorial(e)
            v //= i**e
        PP.append((T, v))
    return PP


def prod(PP, QQ):
    """
    Product of cycle indices
    """
    RR = defaultdict(int)
    for T0, v0 in PP:
        for T1, v1 in QQ:
            T = [0] * (len(T0) * len(T1) + 1)
            for i, e0 in enumerate(T0[1:], 1):
                for j, e1 in enumerate(T1[1:], 1):
                    T[lcm(i, j)] += gcd(i, j) * e0 * e1
            RR[tuple(T)] += v0 * v1
    return list(RR.items())


def solution(w, h, s):
    PP = cycle_index(w)
    QQ = cycle_index(h)
    RR = prod(PP, QQ)

    ans = sum(v * s ** sum(T) for T, v in RR)
    ans //= factorial(w) * factorial(h)
    return str(ans)


assert solution(2, 2, 2) == "7"
assert solution(2, 3, 4) == "430"
