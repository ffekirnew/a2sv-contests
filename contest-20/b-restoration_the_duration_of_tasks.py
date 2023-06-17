def solve():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        start_times = list(map(int, input().split()))
        finish_times = list(map(int, input().split()))

        # find the durations of each task
        durations = []
        for i in range(0, n):
            start_time = max(start_times[i], (finish_times[i-1] if i > 0 else 0))
            finish_time = finish_times[i]

            durations.append(finish_time - start_time)
        
        print(*durations)


if __name__ == "__main__":
    solve()