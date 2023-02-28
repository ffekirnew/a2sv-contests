n = int(input())
nums = list( map( int, input().split() ) )

pf_sum = [0]
for i in range(len(nums)):
    pf_sum.append(pf_sum[-1] + nums[i])

sf_sum = nums[:]
for i in range(len(nums) - 1, -1, -1):
    sf_sum[i] += sf_sum[i + 1] if i < len(nums) - 1 else 0
sf_sum.append(0)

l, r = 0, len(sf_sum) - 1

while l < r:
    if pf_sum[l] <= sf_sum[r]:
        l += 1
    else:
        r -= 1
    
print(l, len(nums) - r)