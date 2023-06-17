def solve():
    tests = int(input())
    for _ in range(tests):
        num_videos, time = map(int, input().split())
        videos = list(map(int, input().split()))
        videos_value = list(map(int, input().split()))

        largest_value, best_video = 0, -1
        for i, video in enumerate(videos):
            if video <= time and videos_value[i] > largest_value:
                largest_value = videos_value[i]
                best_video = i + 1
            
            time -= 1

        print(best_video)

if __name__ == "__main__":
    solve()