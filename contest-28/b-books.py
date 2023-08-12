def solve():
    n, t = list(map(int, input().split()))
    book_minutes = list(map(int, input().split()))

    max_number = 0

    # sliding window
    time_used = 0
    left = 0
    for right in range(len(book_minutes)):
        time_used += book_minutes[right]

        while time_used > t:
            time_used -= book_minutes[left]
            left += 1

        max_number = max(max_number, right - left + 1)
    
    print(max_number)
        


if __name__ == "__main__":
    solve()