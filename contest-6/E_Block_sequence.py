from heapq import heappop, heappush
from math import inf


def solve():
    n, m = list(map(int, input().split()))
    stacks = list(map(int, input().split()))

    answer = 0

    priority_stacks = []
    for i, stack in enumerate(stacks):
        heappush(priority_stacks, (-1 * stack, i))
    
    for i in range(n):
        curr_stack, curr_index = heappop(priority_stacks)
        curr_stack *= -1
        next_stack = (-1 * priority_stacks[0][0]) if priority_stacks else None

        if next_stack:
            if curr_stack != next_stack:
                answer += next_stack
                stacks[curr_index] = curr_stack - next_stack
            elif curr_stack != 1:
                answer += curr_stack - 1
                stacks[curr_index] = 1

    answer += min(sum(stacks[:n - 1]), curr_stack - 1)
    
    print(answer)


if __name__ == "__main__":
    solve()