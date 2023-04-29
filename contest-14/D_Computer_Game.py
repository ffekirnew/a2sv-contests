def solve():
    tests = int(input())
    for _ in range(tests):
        ROWS, COLS = 2, int(input())
        grid = [list(map(int, list(input()))) for _ in range(ROWS)]

        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        IN_BOUND = lambda row, col: 0 <= row < ROWS and 0 <= col < COLS
    
        fringe = [(0, 0)]
        visited = set([(0, 0)])

        answer = "NO"

        while fringe:
            next_level = []

            for row, col in fringe:
                if (row, col) == (1, COLS - 1):
                    answer = "YES"
                    break
                for r, c in DIRS:
                    nx_row, nx_col = row + r, col + c

                    if IN_BOUND(nx_row, nx_col) and (nx_row, nx_col) not in visited and grid[nx_row][nx_col] == 0:
                        visited.add((nx_row, nx_col))
                        next_level.append((nx_row, nx_col))
            
            fringe = next_level
        
        print(answer)


if __name__ == "__main__":
    solve()