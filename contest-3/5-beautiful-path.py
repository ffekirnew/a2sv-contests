dirs = [ [0, -1], [0, 1], [1, 0], [-1, 0] ]

def grid_updater(matrix, start_cell, to_char, dont_touch_char):
    matrix_rows, matrix_cols = len(matrix), len(matrix[0])

    for dir in dirs:
        row, col = start_cell
        while 0 <= row < matrix_rows and 0 <= col < matrix_cols:
            if matrix[row][col] == '*':
                break
            elif matrix[row][col] != dont_touch_char:
                matrix[row][col] = to_char

            row += dir[0]
            col += dir[1]

if __name__ == "__main__":
    rows, cols = map(int, input().split())

    grid = []
    start, target = None, None
    for r in range(rows):
        row = list(input())
        if 'S' in row: start = [r, row.index('S')]
        if 'T' in row: target = [r, row.index('T')]
        grid.append(row)

    # turn open-roads to 'S' starting from s
    grid_updater(matrix=grid, start_cell=start, to_char='S', dont_touch_char='T')

    # turn open-roads to 'T' starting from T
    grid_updater(matrix=grid, start_cell=target, to_char='T', dont_touch_char='S')

    print(grid)
    # find the 'S...T' pattern
    for r in range(rows):
        first_T, first_S, first_block = None, None, None
        for c in range(cols):
            first_T = c if (not first_T and grid[r][c] == 'T') else None
            first_S = c if (not first_T and grid[r][c] == 'S') else None
            block = c if (grid[r][c] == '*') else None
        
        if first_S and first_T:
            if not first_block or first_T < first_block < first_S or first_S < first_block < first_T:
                print("YES")
    
    
    print("NO")
    exit()

