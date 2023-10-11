def solve():
    original_handles = {}
    reversed_handles = {}

    number_of_requests = int(input())
    for _ in range(number_of_requests):
        old, new = input().split()

        if old in reversed_handles:
            original_handles[reversed_handles[old]] = new
            reversed_handles[new] = reversed_handles[old]
        else:
            original_handles[old] = new
            reversed_handles[new] = old

    print(len(list(original_handles)))
    for key, value in original_handles.items():
        print(key, value)


if __name__ == "__main__":
    solve()
