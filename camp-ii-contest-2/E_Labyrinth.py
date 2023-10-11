from heapq import heappop, heappush


def solve():
    ROWS, COLS = list(map(int, input().split()))
    STARTING_CELL_ROW, STARTING_CELL_COL = list(map(int, input().split()))
    ALLOWED_LEFT, ALLOWED_RIGHT = list(map(int, input().split()))
    GRID = [input() for _ in range(ROWS)]

    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def is_in_bound(row: int, col: int) -> bool:
        return 0 <= row < ROWS and 0 <= col < COLS

    distances = [[float("inf")] * COLS for _ in range(ROWS)]
    distances[STARTING_CELL_ROW - 1][STARTING_CELL_COL - 1] = 0

    visited = set()
    root_level = [
        (STARTING_CELL_ROW - 1, STARTING_CELL_COL - 1, ALLOWED_LEFT, ALLOWED_RIGHT)
    ]
    while root_level:
        children_level = []

        for row, col, allowed_left, allowed_right in root_level:
            for r, c in dirs:
                nx_row, nx_col = row + r, col + c

                if (
                    not is_in_bound(nx_row, nx_col)
                    or GRID[nx_row][nx_col] == "*"
                    or (c < 0 and not allowed_left)
                    or (c > 0 and not allowed_right)
                    or (nx_row, nx_col) in visited
                ):
                    continue

                visited.add((nx_row, nx_col))
                children_level.append(
                    (
                        nx_row,
                        nx_col,
                        allowed_left - int(c < 0),
                        allowed_right - int(c > 0),
                    )
                )

        root_level = children_level

    print(len(visited))


if __name__ == "__main__":
    solve()
