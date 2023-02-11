size = int(input())
arr = list(map(int, input().split()))

l, r = 0, 0
reversed_segments = 0

i = 0
while i < size - 1:
    if arr[i + 1] > arr[i]:
        l, r = i, i
        while r < size and arr[r + 1] > arr[r]:
            r += 1
        reversed_segments += 1
        if r == size - 1:
            i = r
        else:
            i = r + 1
    else:
        i += 1
            
if reversed_segments < 2:
    print("yes")
    print(l, r) if reversed_segments else (1, 1)
else:
    print("no")
