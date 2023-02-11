def simulate(grid): 
    n = len(grid)   # num of rows 
    m = len(grid[0]) # num of columns 
  
    # Simulate the process 
    for i in range(n-1): 
        for j in range(m): 
            # Check if the current cell is 'o' 
            if (grid[i][j] == 'o'): 
                # If the cell below is either empty or a 'o' that is already in an immovable state 
                if (grid[i+1][j] == '.' or grid[i+1][j] == 'o'): 
                    # Move it down by replacing it with an empty cell 
                    grid[i][j] = '.' 
                    grid[i+1][j] = 'o'  
  
                else: 
                    # Otherwise, if a '*' cell is encountered, no further movement is possible  
                    break  

    # Print the new state of the grid as output 
    for row in grid: 
        print(''.join(row))  
        
num_tests = int(input())
answers = []

for test in range(num_tests):
    rows, cols = map(int, input().split())
    grid = []

    for r in range(rows):
        grid.append(list(input()))
    simulate(grid)
