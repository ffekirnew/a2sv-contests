import heapq


def prev_power_of_two(n):
    d = 1

    while d * 2 <= n:
        d *= 2

    if d * 2 == n:
        return n
    return d

def solve():
    n, k = list(map(int, input().split()))

    if k > n:
        print("NO")
        exit()

    base_representation = []

    curr_bit = 0
    while n:
        if n % 2:
            base_representation.append(-1 * (n % 2) * (2 ** curr_bit))

        curr_bit += 1
        n >>= 1

    heapq.heapify(base_representation)
    
    if k < len(base_representation):
        print("NO")
        return
    
    print("YES")

    left = k - len(base_representation)

    while left:
        to_be_broken = heapq.heappop(base_representation) * -1
        

        if to_be_broken < left:
            for i in range(to_be_broken):
                heapq.heappush(base_representation, -1)
        else:
            parts_needed = prev_power_of_two(left + 1)
            for i in range(parts_needed):
                heapq.heappush(base_representation, -1 * int(to_be_broken / parts_needed))
        
        left = k - len(base_representation)
        
    base_representation = list(map( lambda x: -1 * x, base_representation ))
    print(*base_representation)
    

if __name__ == "__main__":
    # print("hello", 10 ** 9, 2 * 10 ** 5)
    solve()