import sys
import threading
from collections import defaultdict


def solve():
    n, m = list(map(int, input().split()))
    node_statses = list(map(int, input().split()))

    tree = defaultdict(set)
    for _ in range(n - 1):
        node1, node2 = list(map(int, input().split()))
        tree[node1].add(node2)
        tree[node2].add(node1)

    visited = set()

    def dfs(node: int, number_of_consecutive_cats: int):
        if node in visited:
            return 0
        visited.add(node)

        if node_statses[node - 1]:
            number_of_consecutive_cats += node_statses[node - 1]
        else:
            number_of_consecutive_cats = 0

        if number_of_consecutive_cats > m:
            return 0

        if not tree[node]:
            return 1

        count = 0
        for child in tree[node]:
            tree[child].remove(node)
            count += dfs(child, number_of_consecutive_cats)
        return count

    print(dfs(1, 0))


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
solution_thread = threading.Thread(target=solve)
solution_thread.start()
solution_thread.join()
