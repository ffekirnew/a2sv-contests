def solve():
    n, c = map(int, input().split())
    arival_times = list(map(int, input().split()))

    words_on_screen = 1
    for i in range(1, n):
        if arival_times[i] - arival_times[i - 1] <= c:
            words_on_screen += 1
        else:
            words_on_screen = 1
    
    print(words_on_screen)

if __name__ == "__main__":
    solve()