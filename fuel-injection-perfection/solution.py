from collections import deque, defaultdict


def solution(n):
    Q = deque([(int(n), 0)])
    V = defaultdict(bool)
    while Q:
        x, c = Q.popleft()
        if V[x]:
            continue
        V[x] = True

        if x == 1:
            return c
        if x & 1:
            Q.append((x - 1, c + 1))
            Q.append((x + 1, c + 1))
        else:
            Q.append((x // 2, c + 1))
