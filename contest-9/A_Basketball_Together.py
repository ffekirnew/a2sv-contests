import math


n, d = list(map(int, input().split()))
powers = list(map(int, input().split()))

powers.sort()
index = 0

answer = 0
for i in range(n - 1, -1, -1):
    needed = math.ceil(d / powers[i])
    if d % powers[i] == 0:
        needed += 1

    if needed <= i + 1 - index:
        answer += 1
        index += needed - 1
    else:
        break

print(answer)