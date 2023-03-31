from collections import Counter

def solve():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        sticks = list(map(int, input().split()))
        answer_printed = False

        freq = Counter(sticks)
        for val in freq.values():
            if val % 2 != 0:
                print("NO")
                answer_printed = True
                break
        
        sticks.sort()

        l, r = 0, n * 4 - 1
        area = sticks[l] * sticks[r]

        while not answer_printed and l < r:
            if sticks[l] * sticks[r] != area:
                print("NO")
                answer_printed = True
                break
            l += 2
            r -= 2
    
        if not answer_printed:
            print("YES")

if __name__ == "__main__":
    solve()

