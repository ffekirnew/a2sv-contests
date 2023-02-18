def make_grid_beautiful(grid):
    def rotate(grid):
        grid[0][0], grid[0][1], grid[1][0], grid[1][1] = grid[1][0], grid[0][0], grid[1][1], grid[0][1]
        return grid
    
    def check_beautiful(grid):
        if grid[0][0] < grid[0][1] and grid[1][0] < grid[1][1] and grid[0][0] < grid[1][0] and grid[0][1] < grid[1][1]:
            return True
    
    for i in range(4):
        if check_beautiful(grid):
            return "YES"
        else:
            grid = rotate(grid)
    return "NO"


tests = int(input())
answers = []

for test in range(tests):
    grid = [list(map(int, input().split())) for row in range(2)]
    answers.append(make_grid_beautiful(grid))

for ans in answers:
    print(ans)