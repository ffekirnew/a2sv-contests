def merge(l, r, k):
    merged = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i][1] < r[j][1]:
            if r[j][1] - l[i][1] <= k:
                merged.append(l[i])
            i += 1
        else:
            if l[i][1] - r[j][1] <= k:
                merged.append(r[j])
            j += 1

    while i < len(l):
        merged.append(l[i])
        i += 1

    while j < len(r):
        merged.append(r[j])
        j += 1

    return merged


def merge_sort(arr, k):
    if len(arr) < 2:
        return arr

    merged = []

    mid = len(arr) // 2
    left_winners = merge_sort(arr[:mid], k)
    right_winners = merge_sort(arr[mid:], k)
    return merge(left_winners, right_winners, k)


def solve():
    n, k = list(map(int, input().split()))
    players = list(map(int, input().split()))
    players = list(zip([i for i in range(1, 2 ** n + 1)], players))

    print(*sorted(list(index for index, data in merge_sort(players, k))))


if __name__ == "__main__":
    solve()
