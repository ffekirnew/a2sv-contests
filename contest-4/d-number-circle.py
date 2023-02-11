from collections import deque


n = int(input())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

circle = deque()

for i, num in enumerate(nums):
    if i % 2:
        circle.append(num)
    else:
        circle.appendleft(num)

for i in range(n):
    if circle[i - 1] + circle[(i + 1) % n] <= circle[i]:
        print("NO")
        exit()
print("YES")
print(*circle)