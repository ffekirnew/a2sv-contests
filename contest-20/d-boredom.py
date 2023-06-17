import sys
import threading

def solve():
    length = int(input())
    nums = list(map(int, input().split()))
    
    all_nums = [0] * (max(nums) + 1)
    for num in nums:
        all_nums[num] += 1
    
    memo = {}
    def find_max_score(i):
        if i >= len(all_nums):
            return 0
        
        if i in memo:
            return memo[i]
        
        memo[i] = all_nums[i] * i + max(find_max_score(i + 2), find_max_score(i + 3))

        return memo[i]
    
    print(max(find_max_score(1), find_max_score(2)))

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
solution_thread = threading.Thread(target = solve)
solution_thread.start()
solution_thread.join()
