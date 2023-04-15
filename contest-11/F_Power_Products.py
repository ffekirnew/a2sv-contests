from collections import Counter, defaultdict


def prime_factorization(n, k):
    factorization = []

    d = 2

    while d * d <= n:
        while n % d == 0:
            factorization.append(d)
            n //= d

        d += 1
    
    if n > 1:
        factorization.append(n)

    clean = 1
    left = 1

    freq = Counter(factorization)
    for key, power in freq.items():
        if power != k:
            left *= key ** (k - (power % k))
            clean *= key ** (power % k)
    
    return clean, left

def solve():
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    answer = 0

    seen_before = defaultdict(int)
    for num in nums:
        clean, left = prime_factorization(num, k)

        answer += seen_before[left]

        seen_before[clean] += 1

    print(answer)

if __name__ == "__main__":
    solve()