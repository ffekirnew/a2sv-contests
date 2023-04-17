def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort(key=lambda x: [x < 0, x])

    answer = 0

    count_negatives = 0
    count_zeros = 0
    for num in nums:
        count_negatives += num < 0
        count_zeros += num == 0
    
    if count_negatives % 2 and not count_zeros:
        answer += 1 - nums.pop()

    for num in nums:
        answer += min(abs(1 - num), abs(-1 - num))
    
    print(answer)

if __name__ == "__main__":
    solve()