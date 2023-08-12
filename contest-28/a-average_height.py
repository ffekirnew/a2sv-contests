def solve():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        heights = list(map(int, input().split()))

        heights.sort(key=lambda x: x % 2, reverse=True)

        print(*heights)

if __name__ == "__main__":
    solve()