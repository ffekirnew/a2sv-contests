import sys
import threading

def solve():
    ROWS, COLS = list(map(int, input().split()))
    DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    def in_bound(row, col):
        return 0 <= row < ROWS and 0 <= col < COLS
    
    grid = [list(input()) for _ in range(ROWS)]

    def dfs(row, col, path):
        if (row, col) in visited:
            if (row, col) != path[-2]:
                return True
            return False

        visited.add((row, col))
        for r, c in DIRS:
            nx_row, nx_col = row + r, col + c

            if not in_bound(nx_row, nx_col) or grid[row][col] != grid[nx_row][nx_col]:
                continue

            if dfs(nx_row, nx_col, path + [(row, col)]):
                return True

        return False

    visited = set()
    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) not in visited:
                if dfs(i, j, []):
                    print("Yes")
                    return
    
    print("No")
    return

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
solution_thread = threading.Thread(target = solve)
solution_thread.start()
solution_thread.join()





# from collections import deque
# import sys
# import threading

# def solve():
#     ROWS, COLS = list(map(int, input().split()))
#     DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#     def in_bound(row, col):
#         return 0 <= row < ROWS and 0 <= col < COLS
    
#     grid = [list(input()) for _ in range(ROWS)]
#     in_degree = [[0 for _ in range(COLS)] for _ in range(ROWS)]

#     def dfs(row, col):
#         queue = deque([(row, col)])
#         while queue:
#             print('here')
#             row, col = queue.popleft()

#             if (row, col) in visited:
#                 continue

#             visited.add((row, col))

#             for r, c in DIRS:
#                 nx_row, nx_col = row + r, col + c

#                 if not in_bound(nx_row, nx_col) or grid[row][col] != grid[nx_row][nx_col]:
#                     continue

#                 queue.append((row, col))

#                 in_degree[nx_row][nx_col] += 1

#     visited = set()
#     for r in range(ROWS):
#         for c in range(COLS):
#             if (r, c) not in visited:
#                 visited.add((r, c))
#                 dfs(r, c)
    
#     print(in_degree)

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# solution_thread = threading.Thread(target = solve)
# solution_thread.start()
# solution_thread.join()