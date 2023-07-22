def solve():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        b = list(map(int, input().split()))

        memo = {}
        def dp(index, last_index):
            if (index, last_index) in memo:
                return memo[(index, last_index)]
            elif index > n:
                return False
            elif index == n:
                return b[last_index] == index - last_index - 1
            
            memo[(index, last_index)] = False

            # not using it as a description
            memo[(index, last_index)] |= dp(index + 1, last_index)

            # using it as a description for the next b[index] elements
            memo[(index, last_index)] |= dp(index + b[index] + 1, index)

            # using it as a description for the previous b[index] elements
            if index >= b[index]:
                memo[(index, last_index)] |= dp(index + 1, index)
                # print(b, 'index:', index + 1, 'last_index:', index, 'memo:', memo[(index, last_index)])
            return memo[(index, last_index)]

        print('YES' if dp(0, -1) else 'NO')           


if __name__ == "__main__":
    solve()