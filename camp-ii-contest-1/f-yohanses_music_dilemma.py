def solve():
    number_of_chairs, number_of_hours = list(map(int, input().split()))
    
    matrix = [[0 for _ in range(101)] for __ in range(101)]
    for _ in range(number_of_chairs):
        x, y = list(map(int, input().split()))
        matrix[x][y] += 1

    prefix_sum = []
    for r, row in enumerate(matrix):
        prefix_sum.append([])
        
        for c, cell in enumerate(row):
            pf_before = prefix_sum[r][c-1] if c > 0 else 0
            pf_above = prefix_sum[r-1][c] if r > 0 else 0
            pf_diagonal = prefix_sum[r-1][c-1] if r > 0 and c > 0 else 0
            
            formula = cell + pf_before + pf_above - pf_diagonal
            
            prefix_sum[-1].append(formula)

    for _ in range(number_of_hours):
        row1, col1, row2, col2 = list(map(int, input().split()))

        all_sum = prefix_sum[row2][col2]
        left_sum = prefix_sum[row2][col1 - 1] if col1 > 0 else 0
        top_sum = prefix_sum[row1 - 1][col2] if row1 > 0 else 0
        
        tobe_added_sum = prefix_sum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        
        print(all_sum - left_sum - top_sum + tobe_added_sum)

if __name__ == "__main__":
    solve()