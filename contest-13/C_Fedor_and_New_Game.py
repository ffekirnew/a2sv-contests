

def solve():
    n, m, k = list(map(int, input().split()))
    players = [int(input()) for _ in range(m + 1)]

    num_friends = 0
    fedor = players.pop()

    for player in players:
        xor = fedor ^ player
        diff = 0

        while xor:
            diff += xor % 2
            xor >>= 1

        if diff > k:
            continue

        num_friends += 1

    print(num_friends)


if __name__ == "__main__":
    solve()
