def solve():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        nums = list(map(int, input().split()))

        answer = (2 ** 64) - 1

        for num in nums:
            answer &= num
        
        print(answer)


if __name__ == "__main__":
    solve()