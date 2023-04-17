def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    answer = []

    for i in range(n - 1):
        min_found = False
        min_, min_index = nums[i], None

        for j in range(i + 1, n):
            if nums[j] < min_:
                min_found = True
                min_, min_index = nums[j], j
        
        if min_found:
            nums[i], nums[min_index] = nums[min_index], nums[i]
            answer.append([i, min_index])
    
    print(len(answer))
    for ans in answer:
        print(*ans)

if __name__ == "__main__":
    solve()