n = int(input())
nums = list(map(int, input().split()))

nums.sort()

for i in range(n):
    if nums[i - 1] + nums[(i + 1) % n] <= nums[i]:
        print("NO")
        exit()
print("YES")
print(*nums)