MOD = 10**9 + 7

def solve():
    tests = int(input())
    for _ in range(tests):
        length, change_of_direction = list(map(int, input().split()))

        dp = [[0] * (change_of_direction + 1) for _ in range(length + 1)]
        dp[1][0] = 1

        for i in range(2, length + 1):
            for j in range(change_of_direction + 1):
                dp[i][j] = dp[i - 1][j]

                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD

        # The final answer is the number of paths with the given length and change_of_direction
        # that end at a leaf node (no children)
        final_answer = dp[length][change_of_direction]
        print(2 * final_answer)

if __name__ == "__main__":
    solve()
