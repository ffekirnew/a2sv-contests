def get_divisors(n):
    d = 2
    divisors = []
    while d * d <= n:
        if n % d == 0:
            divisors.append(d)
        d += 1
    
    return divisors

gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
lcm = lambda a, b: a * b // gcd(a, b)

def solve():
    x= int(input())
    divisors = get_divisors(x)

    while divisors and lcm(divisors[-1], x // divisors[-1]) != x:
        divisors.pop()

    if divisors:
        print(divisors[-1], x // divisors[-1])
    else:
        print("1", x)
    

if __name__ == "__main__":
    solve()