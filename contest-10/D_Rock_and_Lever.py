from collections import defaultdict


def solve():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        nums = list(map(int, input().split()))

        bin_rep = [ len(bin(num)) - 2 for num in nums ]

        seen = defaultdict(int)
        answer = 0

        for num in bin_rep:
            if num in seen:
                answer += seen[num]
            seen[num] += 1
        
        print(answer)



if __name__ == "__main__":
    solve()