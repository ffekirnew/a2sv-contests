import heapq
import math

DIMENSION = int(input())
queen_loc = list(map(int, input().split()))
king_loc = list(map(int, input().split()))
GOAL = tuple(map(int, input().split()))

DIRS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]


def checked(row, col):
    diagonal_formula = queen_loc[1] - queen_loc[0]
    anti_diagonal_formula = queen_loc[1] + queen_loc[0]

    diagonal = (col - row) == diagonal_formula
    anti_diagonal = (col + row) == anti_diagonal_formula
    row_check = row == queen_loc[0]
    col_check = col == queen_loc[1]

    return diagonal or anti_diagonal or row_check or col_check


def in_bound(row, col, dimension):
    return 0 <= row < dimension and 0 <= col < dimension


def heuristic(row, col):
    return math.sqrt((row - GOAL[0]) ** 2 + (col - GOAL[1]) ** 2)


def a_star_search():
    fringe = []
    visited = set()
    heapq.heappush(fringe, (0, 0, king_loc[0], king_loc[1]))

    while fringe:
        _, g_score, row, col = heapq.heappop(fringe)

        if (row, col) in visited:
            continue

        if (row, col) == GOAL:
            return True

        visited.add((row, col))

        for r, c in DIRS:
            new_row, new_col = row + r, col + c

            if not in_bound(new_row, new_col, DIMENSION) or checked(new_row, new_col):
                continue

            h_score = heuristic(new_row, new_col)
            new_g_score = g_score + 1
            f_score = new_g_score + h_score

            heapq.heappush(fringe, (f_score, new_g_score, new_row, new_col))

    return False


if a_star_search():
    print("YES")
else:
    print("NO")
