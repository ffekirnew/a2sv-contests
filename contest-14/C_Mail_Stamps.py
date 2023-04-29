from collections import defaultdict, deque
import sys
import threading

def main():
    stamps = int(input())
    descriptions = [list(map(int, input().split())) for _ in range(stamps)]
    
    
    graph = defaultdict(list)
    
    for from_, to_ in descriptions:
        graph[from_].append(to_)
        graph[to_].append(from_)
    
    nodes = [(key, value) for key, value in graph.items()]
    nodes.sort(key=lambda x: len(x[1]))

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        path.append(node)

        for child in graph[node]:
            dfs(child)
    
    path = []
    visited = set()
    dfs(nodes[0][0])
    print(*path)

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()