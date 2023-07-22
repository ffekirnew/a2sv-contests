def solve():
    tests = int(input())
    for _ in range(tests):
        n, m = list(map(int, input().split()))

        if n % 2 == 0 and m % 2 == 0:
            print('abdullah')
        else:
            print('hasan')

if __name__ == "__main__":
    solve()
