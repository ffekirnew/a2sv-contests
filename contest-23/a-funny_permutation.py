def solve():
    tests = int(input())
    for _ in range(tests):
        n = int(input())

        if n in [1, 3]:
            print("-1")
            continue
        
        funny_permutation = [i for i in range(n, 0, -1)]
        if n % 2 != 0:
            funny_permutation[n // 2], funny_permutation[n // 2 - 1] = funny_permutation[n // 2 - 1], funny_permutation[n // 2]

        print(*funny_permutation)

if __name__ == "__main__":
    solve()