from collections import Counter, defaultdict


def solve():
    n, amount = list(map(int, input().split()))
    coins = set(map(int, input().split()))
    counter_coins = Counter(coins)

    answer = set({0, amount})

    memo = {}

    def dp(amount, curr_coins):
        nonlocal answer
        if amount <= 0:
            answer = answer.union(curr_coins)
            return amount == 0

        if amount in memo:
            return memo[amount]

        for coin in coins:
            if counter_coins[coin] > curr_coins.get(coin, 0):
                curr_coins[coin] -= 1
                added = dp(amount - coin, curr_coins)
                curr_coins[coin] += 1
                if added:
                    answer.add(amount - coin)

    dp(amount, defaultdict(int))
    print(answer)


if __name__ == "__main__":
    solve()
