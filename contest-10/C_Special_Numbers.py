def solve():
    tests = int(input())
    for _ in range(tests):
        n, k = list(map(int, input().split()))

        answer = 0

        curr_bit = 0

        while k:
            if k % 2:
                answer += n ** curr_bit

            curr_bit += 1
            k >>= 1
        
        print(answer % (10 ** 9 + 7))

if __name__ == "__main__":
    solve()