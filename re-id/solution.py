def get_primes(n):
    is_prime = [True] * n
    for i in range(2, n):
        if not is_prime[i]:
            continue
        yield i
        for j in range(i + i, n, i):
            is_prime[j] = False


def solution(i):
    assert 0 <= i <= 10000
    primes = "".join(map(str, get_primes(100000)))
    assert len(primes) > 10000 + 5
    return primes[i : i + 5]
