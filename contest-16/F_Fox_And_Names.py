from collections import defaultdict, deque


def solve():
    n = int(input())
    names = [input() for _ in range(n)]
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for index in range(n - 1):
        name1, name2 = names[index], names[index + 1]

        i = 0
        while i < len(name1) and i < len(name2) and name1[i] == name2[i]:
            i += 1
        
        if i < len(name1) and i < len(name2):
            graph[name1[i]].append(name2[i])
            in_degree[name2[i]] += 1
    
    print(graph)

    # def dfsCycle(node, parent):
    #     visited.add(node)
        
    #     for child in graph[node]:
    #         if child not in visited:
    #             if dfsCycle(child, node):
    #                 return True
                    
    #         elif child != parent:
    #             return True
                
    #     return False

    # is_cycle = False
    # visited = set()
    # for i in list(graph.keys()):
    #     if i not in visited:
    #         if dfsCycle(i, -1):
    #             is_cycle = True
    #             break
    
    # if is_cycle:
    #     print("Impossible")
    #     return
    
    # color = {i: 0 for i in range(26)}
    # order = []
    # stack = [course for course in graph if in_degree[course] == 0]
    
    # for course in stack:
    #     if color[course] == 'g':
    #         break

    #     if color[course] == 'w':
    #         dfs(course)

if __name__ == "__main__":
    solve()