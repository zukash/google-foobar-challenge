import numpy as np
from numpy.linalg import matrix_power
from fractions import Fraction


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def convert2ratio(X):
    X = [Fraction(x).limit_denominator() for x in X]
    common_deno = 1
    for x in X:
        common_deno = lcm(common_deno, x.denominator)
    return [x.numerator * common_deno // x.denominator for x in X]


def solution(G):
    G = np.array(G, dtype=np.float64)
    for u in range(len(G)):
        # terminal state
        if sum(G[u]) == 0:
            G[u][u] = 1
        # normalize
        G[u] /= sum(G[u])

    G = matrix_power(G, 1 << 128)
    R = convert2ratio([x for i, x in enumerate(G[0]) if G[i][i] == 1])
    return R + [sum(R)]
