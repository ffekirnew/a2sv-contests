import sys
import threading


def solve():
    n = int(input())
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))

    memo = {}
    def dp(row, col):
        if col == n:
            return 0

        if (row, col) in memo:
            return memo[(row, col)]

        if row == 0:
            memo[(row, col)] = max(row1[col] + dp(1, col + 1), dp(0, col + 1))
        else:
            memo[(row, col)] = max(row2[col] + dp(0, col + 1), dp(1, col + 1))

        return memo[(row, col)]
    
    print(max(dp(0, 0), dp(1, 0)))

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
solution_thread = threading.Thread(target = solve)
solution_thread.start()
solution_thread.join()