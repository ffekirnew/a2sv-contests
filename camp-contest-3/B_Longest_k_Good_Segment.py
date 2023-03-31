from collections import defaultdict


n, k = map(int, input().split())
arr = list(map(int, input().split()))

diff = defaultdict(int)

l = 0
max_len = 0
answer = None

for r in range(n):
    diff[arr[r]] += 1

    while len(diff) > k:
        diff[arr[l]] -= 1

        if not diff[arr[l]]:
            del diff[arr[l]]
        
        l += 1
    
    if r - l + 1 > max_len:
        max_len = max(max_len, r - l + 1)
        answer = [l + 1, r + 1]

print(*answer)

