if __name__ == "__main__":
    ways = 0

    n, m, k = map( int, input().split() )

    grid = []
    for row in range(n):
        grid.append( list( input() ) )
    
    if k == 1:
        for row in grid:
            ways += row.count('.')
            
        print(ways)
        exit()

    # go through each row with a sliding window
    for row in grid:
        r = k
        curr = row[ r - k : r ].count('.')
        ways += 1 if curr == k else 0

        while r < m:
            curr += 1 if row[r] == '.' else 0
            curr -= 1 if row[r - k] == '.' else 0
            ways += 1 if curr == k else 0
            r += 1

    # go through each column
    for col in range(m):
        curr = 0
        for i in range(k):
            if i < n:
                curr += 1 if grid[i][col] == '.' else 0
        ways += 1 if curr == k else 0

        r = k
        while r < n:
            curr += 1 if grid[r][col] == '.' else 0
            curr -= 1 if grid[r - k][col] == '.' else 0
            ways += 1 if curr == k else 0
            r += 1
    
    print(ways)
    exit()
