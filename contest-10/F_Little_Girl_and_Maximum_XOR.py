def solve():
    n, k = list(map(int, input().split()))

    furthest_alternating_degree = -1

    curr_bit = 0
    while n or k:
        if n % 2 != k % 2:
            furthest_alternating_degree = curr_bit

        curr_bit += 1
        n >>= 1
        k >>= 1
        
    answer = 0

    while furthest_alternating_degree > -1:
        answer += 2 ** furthest_alternating_degree

        furthest_alternating_degree -= 1
    
    print(answer)

if __name__ == "__main__":
    solve()