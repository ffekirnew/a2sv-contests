from collections import defaultdict


num_tests = int(input())
answers = []

for test in range(num_tests):
    nums = input()

    freq = defaultdict(int)

    l, r = 0, 0
    min_len = float('inf')

    while r < len(nums):
        freq[nums[r]] += 1

        while len(freq) == 3 and l < r and freq[nums[l]] > 1:
            freq[nums[l]] -= 1
            l += 1
        
        if len(freq) == 3:
            min_len = min(min_len, r - l + 1)

        r += 1
    
    answers.append(min_len if min_len != float('inf') else 0)

for ans in answers:
    print(ans)