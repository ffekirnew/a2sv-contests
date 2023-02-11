n = int(input())
nums = list(map(int, input().split()))

w, h = 0, 0

l, r = 0, len(nums) - 1
turn = 0

while l <= r:
    if turn % 2 == 0:
        if nums[l] > nums[r]:
            w +=  nums[l]
            l += 1
        else:
            w += nums[r]
            r -= 1
    else:
        if nums[l] > nums[r]:
            h +=  nums[l]
            l += 1
        else:
            h += nums[r]
            r -= 1
    turn += 1
    
print(w, h)
