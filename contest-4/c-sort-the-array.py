size = int(input())
array = list(map(int, input().split()))

l, r = 0, 0
used = False

i = 1
while i < size:
    if array[i] < array[i - 1]:
        if not used:
            used = True
            l, r = i - 1, i
            while r < size and array[r] < array[r - 1]:
                r += 1
            i = r
        else:
            print("no")
            exit()
    else:
        i += 1

print("yes")
print(l + 1, r)
exit()

