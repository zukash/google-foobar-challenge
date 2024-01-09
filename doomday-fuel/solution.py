from fractions import Fraction


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def convert_to_integer_ratio(X):
    common_deno = 1
    for x in X:
        common_deno = lcm(common_deno, x.denominator)
    return [x.numerator * common_deno // x.denominator for x in X]


def solution(G):
    n = len(G)
    for u in range(n):
        total = sum(G[u])
        if total == 0:
            continue
        G[u] = [Fraction(p, total) for p in G[u]]

    stack = [u for u in range(n) if G[0][u] != 0]
    while stack:
        u = stack.pop()
        if u == 0:
            continue

        if sum(G[u]) == 0:
            continue

        for v in range(n):
            # 0 -> u -> v => 0 -> v
            G[0][v] += G[0][u] * G[u][v]
            G[u][v] = 0
            stack.append(v)
        G[0][u] = 0

    R = convert_to_integer_ratio(G[0][2:])
    return R + [sum(R)]


# OK
assert solution(
    [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
) == [0, 3, 2, 9, 14]

# OK
assert solution(
    [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
) == [7, 6, 8, 21]

# NG
assert solution(
    [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
) == [0, 0, 1, 1]
