import sys
from math import inf


def solve():
    n, m = list(map(int, input().split()))
    cities = list(map(int, sys.stdin.readline().split()))
    towers = list(map(int, sys.stdin.readline().split()))

    farthest_cities = [] 

    # going forward
    for tower in towers:
        # find left city
        left, right = 0, n - 1
        while left < right:
            city = cities[left + (right - left) // 2]
            if city < tower:

        
        # find right city
        left, right = 0, n - 1
    

    min_distance = 0
    for i, tower in enumerate(towers):
        left_city, right_city = (
            tower - farthest_cities[i][0],
            farthest_cities[i][1] - tower,
        )
        left_city_to_left_tower, right_city_to_right_tower = (
            abs(towers[i - 1] - farthest_cities[i][0]) if (i > 0) else inf,
            abs(farthest_cities[i][1] - towers[i + 1]) if (i < m - 1) else inf,
        )

        if left_city < left_city_to_left_tower:
            min_distance = max(min_distance, left_city)
        if right_city < right_city_to_right_tower:
            min_distance = max(min_distance, right_city)

    print(min_distance)


if __name__ == "__main__":
    solve()
