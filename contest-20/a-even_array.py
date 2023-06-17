def solve():
    tests = int(input())
    for _ in range(tests):
        length = int(input())
        init_array = list(map(int, input().split()))
        
        # count out of place odds and evens
        out_of_place_odds, out_of_place_evens = 0, 0
        for i, num in enumerate(init_array):
            if i % 2 != num % 2:
                if i % 2 == 0:
                    out_of_place_evens += 1
                else:
                    out_of_place_odds += 1
        
        if out_of_place_odds != out_of_place_evens:
            print(-1)
        else:
            print(out_of_place_evens)

if __name__ == "__main__":
    solve()