import heapq


def solve():
    tests = int(input())
    for _ in range(tests):
        n, m = list(map(int, input().split()))

        nums = list(map(int, input().split()))
        heapq.heapify(nums)

        changes = list(map(int, input().split()))

        for change in changes:
            heapq.heappop(nums)
            heapq.heappush(nums, change)
        
        print(sum(nums))

if __name__ == "__main__":
    solve()
