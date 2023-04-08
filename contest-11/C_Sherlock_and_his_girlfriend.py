def sieve(n):
    color = [1] * (n)
    is_prime = [True] * (n)

    d = 2  
    curr_color = 2
    while d - 2 < n:
        if is_prime[d - 2]:
            j = d * d

            while j - 2 < n:
                is_prime[j - 2] = False
                color[j - 2] = curr_color
                j += d
        d += 1
    
    return color

def solve():
    n = int(input())
    coloring = sieve(n)

    print(1 if n < 3 else 2)
    print(*coloring)

if __name__ == "__main__":
    solve()