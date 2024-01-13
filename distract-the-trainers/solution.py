import networkx as nx
from itertools import combinations


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def check(a, b):
    g = gcd(a, b)
    a, b = a // g, b // g
    return a + b != 1 << ((a + b).bit_length() - 1)


def solution(L):
    G = nx.Graph()
    for a, b in combinations(L, 2):
        if check(a, b):
            G.add_edge(a, b)
    matching = nx.max_weight_matching(G, maxcardinality=True)
    return len(L) - len(matching) * 2


assert solution([1, 7, 3, 21, 13, 19]) == 0
assert solution([1, 1]) == 2


# def naive(a, b):
#     S = set()
#     while a != b:
#         if (a, b) in S:
#             return True
#         S.add((a, b))
#         if a > b:
#             a -= b
#             b += b
#         else:
#             b -= a
#             a += a
#         # print(a, b)
#     return False

# MAX = 1 << 8
# S = set()
# for a in range(1, MAX):
#     for b in range(a, MAX):
#         assert naive(a, b) == check(a, b)
#         if naive(a, b):
#             S.add((a, b))
