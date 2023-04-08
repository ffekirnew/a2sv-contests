tests = int(input())
for _ in range(tests):
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(len(nums)):
        xor = 0
        for j in range(len(nums)):
            if j != i:
                xor ^= nums[j]
        
        if nums[i] == xor:
            print(nums[i])
            break
