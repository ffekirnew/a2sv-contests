length = int(input())
days = list(map(int, input().split()))

l, r = 0, 1
maximum = 0
if length == 1:
    print(1)
    exit()

while r < length:
    if days[r] < days[r - 1]:
        l = r
    
    maximum = max(r - l + 1, maximum)
    r += 1

print(maximum)
