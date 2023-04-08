from bisect import bisect_left, bisect_right
from collections import deque

def get_divisors(n):
    d = 2
    latest = None
    while d * d <= n:
        if n % d == 0:
            latest = d
        d += 1
    
    return latest


def solve():
    a, b = list(map(int, input().split()))
    a, b = min(a, b), max(a, b)

    a_divisors = get_divisors(a)
    a_divisors.sort()
    b_divisors = get_divisors(b)
    b_divisors.sort()

    n = int(input())

    for _ in range(n):
        query = list(map(int, input().split()))

        # binary search on a
        left_most = bisect_left(a_divisors, query[0])
        right_most = bisect_left(a_divisors, query[1])

        greatest = None
        for i in range(left_most, right_most):
            place = bisect_left(b_divisors, a_divisors[i])

            if a_divisors[i] == b_divisors[place]:
                greatest = a_divisors[i]
        
        print("-1" if not greatest else greatest)

if __name__ == "__main__":
    solve()