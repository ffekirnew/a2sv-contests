def check_if_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

n = int(input())
answers = []

for i in range(n):
    ans = 0
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in range(n - k):
        is_good = True
        for j in range(i + 1, i + k + 1):
            if nums[j] * 2 <= nums[j - 1]:
                is_good = False
        if is_good:
            ans += 1
    
    answers.append(ans)

for ans in answers:
    print(ans)


    