def solve():
    num_cards= int(input())

    mati_cards = list(map(int, input().split()))
    ibsa_cards = list(map(int, input().split()))

    mati_cards.sort()
    ibsa_cards.sort()

    mati_turn, ibsa_turn = 0, 0
    points = 0
    
    while mati_turn < num_cards and ibsa_turn < num_cards:
        if mati_cards[mati_turn] <= ibsa_cards[ibsa_turn]:
            mati_turn += 1
            ibsa_turn += 1
            points += 1
        else:
            ibsa_turn += 1
            points -= 1
    
    print("YES" if points > 0 else "NO")
    

if __name__ == "__main__":
    solve()