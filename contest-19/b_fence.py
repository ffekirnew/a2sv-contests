from math import inf


def solve():
    n, k = list(map(int, input().split()))
    fences = list(map(int, input().split()))
    answer = 0

    min_sum = inf
    curr_sum = 0
    l = 0
    for r in range(n):
        curr_sum += fences[r]
        if r - l == k:
            curr_sum -= fences[l]
            l += 1

        if r - l + 1 == k and curr_sum < min_sum:
            min_sum = curr_sum
            answer = l + 1

    
    print(answer)



if __name__ == "__main__":
    solve()