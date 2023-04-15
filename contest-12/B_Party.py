from collections import defaultdict
    
            
    
def solve():
    n = int(input())
    managers = [ [i, int(input())] for i in range(1, n + 1) ]
    
    graph = {i: [] for i in range(1, n + 1) }
    
    for subordinate, manager in managers:
        if manager != -1:
            graph[manager].append(subordinate)
    
    def dfs(node, group=1):
        bi_partite[group].add(node)
        visited.add(node)
        
        for child in graph[node]:
            dfs(child, group + 1)
    
    bi_partite = defaultdict(set)
    visited = set()
    for i in range(1, n + 1):
        if len(graph[i]) != 0:
            dfs(i)
    
    for i in range(1, n + 1):
        if i not in visited:
            bi_partite[1].add(i)
    
    print(len(bi_partite))
    
if __name__ == "__main__":
    solve()