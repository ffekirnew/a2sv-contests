def solve():
    n, m, p = list(map(int, input().split()))
    grid = [list(input()) for _ in range(n)]
    actions = list(map(int, input().split()))
 
    IN_BOUND = lambda row, col: 0 <= row < n and 0 <= col < m
 
    movements = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
 
    curr_position = [[r, c] for r in range(n) for c in range(m) if grid[r][c] == 'M'][0]
 
    for action in actions:
        movement = movements[action]
        curr_position[0] += movement[0]
        curr_position[1] += movement[1]
 
    answer = 0
    fringe = [(curr_position[0], curr_position[1], 1)]
    visited = set()
    while fringe:
        next_level = []
 
        for row, col, depth in fringe:
            if depth > p:
                continue
            
            for r, c in movements:
                nx_row = row + r
                nx_col = col + c
 
                if IN_BOUND(nx_row, nx_col) and (nx_row, nx_col) not in visited and grid[nx_row][nx_col] != '#':
                    visited.add((nx_row, nx_col))
                    next_level.append((nx_row, nx_col, depth + 1))
                    answer += 1
        
        fringe = next_level
    
    print(answer)
    return
 
 
    
 
 
if __name__ == "__main__":
    solve()