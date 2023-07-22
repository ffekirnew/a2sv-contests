from collections import defaultdict


def solve():
    num_nodes, num_edges, num_forbidden = list(map(int, input().split()))
    
    # convert to adjacency list representation
    graph = defaultdict(list)
    for _ in range(num_edges):
        edge = list(map(int, input().split()))
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    forbidden = {}
    for _ in range(num_forbidden):
        from_, through_, to_ = list(map(int, input().split()))
        if from_ not in forbidden:
            forbidden[from_] = defaultdict(set)
        forbidden[from_][through_].add(to_)
    
    root_level = [[1, [1]]]
    visited_once = set()
    visited_twice = set()

    while root_level:
        print(root_level)
        children_level = []

        for curr_node, curr_path in root_level:
            if curr_node == num_nodes:
                print(len(curr_path) - 1)
                print(*curr_path)
                return

            for child in graph[curr_node]:
                print(child, visited_once, visited_twice) if curr_node == 3 else None
                visited_once.add(child)
                if child in visited_twice:
                    continue
                if child in visited_once:
                    visited_twice.add(child)
                if len(curr_path) > 1:
                    if curr_path[-2] in forbidden:
                        if curr_path[-1] in forbidden[curr_path[-2]]:
                            if child in forbidden[curr_path[-2]][curr_path[-1]]:
                                print('here')
                                continue
                    children_level.append([child, curr_path + [child]])
                else:
                    children_level.append([child, curr_path + [child]])
        
        root_level = children_level

    print(-1)
    return  

if __name__ == "__main__":
    solve()