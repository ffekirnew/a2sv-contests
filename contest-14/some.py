from collections import defaultdict, deque
import sys


sys.setrecursionlimit(1_000_000)

def solve():
    stamps = int(input())
    descriptions = [list(map(int, input().split())) for _ in range(stamps)]
    
    
    graph = defaultdict(list)
    
    for from_, to_ in descriptions:
        graph[from_].append(to_)
        graph[to_].append(from_)
    
    nodes = [(key, value) for key, value in graph.items()]
    nodes.sort(key=lambda x: len(x[1]))

    
    def dfs(node):
        path.append(node)

        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                dfs(child)

    
    path = []
    visited = set()
    dfs(nodes[0][0])
    print(*path)
    
    
if __name__ == "__main__":
    solve()