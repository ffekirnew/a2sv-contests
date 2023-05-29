import sys
import threading
from collections import defaultdict, deque


def solve():
    num_nodes, num_edges = map(int, sys.stdin.readline().split())
    edges = [sys.stdin.readline().split() for _ in range(num_edges)]
    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Detect cycle in the graph and color it
    color = defaultdict(int)  # 0 for color A, 1 for color B

    def color_graph(node, node_color):
        color[node] = node_color
        
        for child in graph[node]:
            if child not in color:
                if color_graph(child, 1 - node_color):
                    return True
            elif color[node] == color[child]:
                return True
        
        return False

    for i in graph.keys():
        if i not in color:
            if color_graph(i, 0):
                print("NO")
                return
    
    answer = []
    for edge in edges:
        answer.append("1" if color[edge[0]] == 0 else "0")
    
    print("YES")
    print("".join(answer))
    return


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
solution_thread = threading.Thread(target=solve)
solution_thread.start()
solution_thread.join()
