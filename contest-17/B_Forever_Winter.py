from collections import defaultdict, deque

def solve():
    tests = int(input())
    for _ in range(tests):
        n, m = list(map(int, input().split()))
        degree = defaultdict(int)
        adj_list = defaultdict(list)

        for _ in range(m):
            from_, to_ = list(map(int, input().split()))
            degree[from_] += 1
            degree[to_] += 1
            adj_list[from_].append(to_)
            adj_list[to_].append(from_)
            
        queue = deque([key for key in adj_list if degree[key] == 1])
        while queue:
            node = queue.popleft()

            for child in adj_list[node]:
                degree[child] -= 1

                if degree[child] == 1:
                    queue.append(child)
        
        center = node
        second_level = adj_list[center][0]

        x = len(adj_list[center])
        y = len(adj_list[second_level])

        print(x, y - 1)

if __name__ == "__main__":
    solve()