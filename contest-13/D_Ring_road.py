from collections import defaultdict
from math import inf


def dfs(start, path_starter, graph, total_cost, visited):
    for target, cost in graph[start].items():
        if (target == 1 and start != path_starter) or target not in visited:
            visited.add(target)

            if cost < 0:
                total_cost[0] += -cost

            if target == 1 and start != path_starter:
                break

            dfs(target, path_starter, graph, total_cost, visited)


def solve():
    nodes = int(input())
    roads = defaultdict(dict)

    for _ in range(nodes):
        a, b, cost = list(map
                          (int, input().split()))
        roads[a][b] = cost
        if len(roads[b]) < 2:
            roads[b][a] = -cost

    answer = inf
    for key, value in roads[1].items():
        total_cost = [-1 * value if value < 0 else 0]
        visited = set([1, key])
        dfs(key, key, roads, total_cost, visited)
        answer = min(answer, total_cost[0])

    print(answer)


if __name__ == "__main__":
    solve()
