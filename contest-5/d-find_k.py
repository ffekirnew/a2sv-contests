from collections import defaultdict


num_tests = int(input())
answers = []

for test in range(num_tests):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    total_sum = sum(arr)

    if (total_sum == n * k): 
        answers.append("YES")
        break

    for i in range(n - 1): 
        if (abs(arr[i] - arr[i+1]) == k): 
            answers.append("YES")

    if len(answers) == test:
        answers.append("NO")

for ans in answers:
    print(ans)