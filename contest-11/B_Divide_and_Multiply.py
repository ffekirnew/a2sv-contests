def solve():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        array = list(map(int, input().split()))
        max_sum = 0

        for i in range(n):
            for j in range(n):
                if i is not j:
                    while array[j] % 2 == 0:
                        array[i] *= 2
                        array[j] //= 2
            max_sum = max( max_sum, sum(array) )
        
        print(max_sum)

if __name__ == "__main__":
    solve()