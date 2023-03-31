n, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

curr = 1 << n


for i in range(n):
    if nums[i] == 0:
        curr -= 1
    else:
        curr += 1


print(curr)
