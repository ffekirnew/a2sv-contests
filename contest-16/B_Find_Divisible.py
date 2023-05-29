def solve():
    tests = int(input())
    for _ in range(tests):
        l, r = list(map(int, input().split()))
        print(l, l * 2)

if __name__ == "__main__":
    solve()