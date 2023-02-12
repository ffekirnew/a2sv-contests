if __name__ == "__main__":

    n = int(input())
    nums = list( map( int, input().split() ) )

    nums.sort()

    sums = [0, 0]

    for i in range(2 * n):
        sums[0 if i < n else 1] += nums[i]

    if sums[0] == sums[1]:
        print("-1")
    else:
        print(*nums)