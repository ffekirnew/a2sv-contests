def beautiful_grid(grid):
    pass

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        grid = [list(map(int, input().strip())) for _ in range(n)]
        print(beautiful_grid(grid))