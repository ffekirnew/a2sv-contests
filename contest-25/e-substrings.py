from collections import defaultdict, deque

def topological_sort_bfs(graph, indegree):
    result = []
    queue = deque()

    for node in graph.keys():
        if indegree[node] == 0:
            queue.append(node)

    while queue:
        current_node = queue.popleft()
        result.append(current_node)

        for neighbor in graph[current_node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph):
        return None

    return result

def solve():
    num_nodes, num_edges = list(map(int, input().split()))
    nodes = input()
    
    # convert to adjacency list representation
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for _ in range(num_edges):
        edge = list(map(int, input().split()))
        graph[edge[0]].append(edge[1])
        indegree[edge[1]] += 1
    
    top_sort_result = topological_sort_bfs(graph, indegree)

    if top_sort_result is None:
        print(-1)
    else:
        for node in range(1, num_nodes + 1):
            root_level = []
            chars = {nodes[node - 1] : 1}
            stack = [node, chars]

            while root_level:
                children_level = []

                for node, chars in root_level:
                    for child in graph[node]:
                        chars[nodes[child - 1]] = 1
                        children_level.append([child, chars.copy()])
                        chars[node[child - 1]] = 0
                
                root_level = children_level


if __name__ == "__main__":
    solve()
