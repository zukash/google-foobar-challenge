from collections import deque
from itertools import product


def solution(src, dest):
    si, sj = divmod(src, 8)
    ti, tj = divmod(dest, 8)

    dq = deque([(si, sj, 0)])
    visited = {(si, sj)}
    while dq:
        i, j, dist = dq.popleft()
        if i == ti and j == tj:
            return dist
        for di, dj in product([-2, -1, 1, 2], repeat=2):
            if di**2 + dj**2 != 5:
                continue
            ni, nj = i + di, j + dj
            if not (0 <= ni < 8 and 0 <= nj < 8):
                continue
            if (ni, nj) in visited:
                continue
            visited.add((ni, nj))
            dq.append((ni, nj, dist + 1))
