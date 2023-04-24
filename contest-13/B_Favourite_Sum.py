def solve():
    tests = int(input())
    for _ in range(tests):
        n, x = list(map(int, input().split()))
        nums = list(map(int, input().split()))

        answer = (x * (x + 1)) // 2

        for num in nums:
            if num > x:
                continue
            answer -= (2 * num)

        print(answer)


if __name__ == "__main__":
    solve()
