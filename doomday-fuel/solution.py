from fractions import Fraction


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def convert2ratio(X):
    common_deno = 1
    for x in X:
        common_deno = lcm(common_deno, x.denominator)
    return [x.numerator * common_deno // x.denominator for x in X]


def matrix_prod(A, B, MOD=None):
    ah, aw = len(A), len(A[0])
    bh, bw = len(B), len(B[0])
    assert aw == bh
    C = [[0] * bw for _ in range(ah)]
    for i in range(ah):
        for j in range(bw):
            for k in range(aw):
                C[i][j] += A[i][k] * B[k][j]
    if MOD:
        for i in range(ah):
            for j in range(bw):
                C[i][j] %= MOD
    return C


def matrix_power(A, k):
    if k == 1:
        return A
    AA = matrix_power(matrix_prod(A, A), k // 2)
    if k & 1:
        return matrix_prod(AA, A)
    else:
        return AA


def solution(G):
    n = len(G)
    for u in range(n):
        total = sum(G[u])
        if total == 0:
            G[u][u] = 1
        else:
            G[u] = [float(p) / total for p in G[u]]

    G = matrix_power(G, 1 << 128)
    # eps = 1e-64
    R = [x for i, x in enumerate(G[0]) if G[i][i] == 1]
    R = [Fraction(r).limit_denominator() for r in R]
    R = convert2ratio(R)
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

# OK
assert solution(
    [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
) == [1, 1]
