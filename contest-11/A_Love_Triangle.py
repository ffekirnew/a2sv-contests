def solve():
    n = int(input())
    planes = list(map(int, input().split()))

    liking_dict = {}

    for i in range(n):
        liking_dict[i + 1] = planes[i]

    for i in range(n):
        a_likes = liking_dict[i + 1]
        b_likes = liking_dict[a_likes]
        c_likes = liking_dict[b_likes]

        if c_likes == i + 1:
            print("YES")
            return
    
    print("NO")
    return


if __name__ == "__main__":
    solve()