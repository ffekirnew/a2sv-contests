length = int(input())
students = list(map(int, input().split()))
students.sort()


l, r = 0, 0
maximum = 0

while r < length:
    while students[r] - students[l] > 5:
        l += 1
    
    maximum = max(r - l + 1, maximum)
    r += 1

print(maximum)