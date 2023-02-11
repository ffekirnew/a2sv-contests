from collections import defaultdict


num_tests = int(input())
answers = []

for test in range(num_tests):
    rows, cols = map(int, input().split())
    grid = []

    for r in range(rows):
        grid.append(list(input()))

    for col in range(cols):
        stone_found = False
        for row in range(rows - 1):
            if stone_found:
                if grid[row - 1][col] == 'o':
                    stone_found = False
                else:
                    grid[row][col], grid[row + 1][col] = grid[row + 1][col], grid[row][col]
            else:
                if grid[row][col] == '*':
                    stone_found = True
                    if grid[row - 1][col] == 'o':
                        stone_found = False
                    else:
                        grid[row][col], grid[row + 1][col] = grid[row + 1][col], grid[row][col]

    
    answers.append(grid)

for grid in answers:
    for row in grid:
        print("".join(row))
    print()