def solve():
    tests = int(input())
    for _ in range(tests):
        restored = []

        n = int(input())
        nums = list(map(int, input().split()))

        i, j = 0, n - 1

        while i <= j:
            restored.append(nums[i])
            if i is not j:
                restored.append(nums[j])

            i += 1
            j -= 1
        
        print(*restored)


    

if __name__ == "__main__":
    solve()