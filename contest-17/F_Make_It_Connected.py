import heapq


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def __contains__(self, x):
        return x in self.parent
        

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        stack = []
        while self.parent[x] != x:
            stack.append(x)
            x = self.parent[x]

        # Path compression
        for node in stack:
            self.parent[node] = x

        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

def solve():
    n, offers = list(map(int, input().split()))
    node_costs = list(map(int, input().split()))

    nodes = sorted(list(zip(node_costs, [i + 1 for i in range(n)])))
    # print(nodes)

    costs = []

    for i in range(1):
        for j in range(i + 1, n):
            heapq.heappush(costs, (nodes[i][0] + nodes[j][0], nodes[i][1], nodes[j][1]))

    if offers:
        for _ in range(offers):
            x, y, w = list(map(int, input().split()))
            if min(x, y) != nodes[0][0]:
                heapq.heappush(costs, ((min(node_costs[x - 1], node_costs[y - 1]) + nodes[0][0]) + w, x, y))
            heapq.heappush(costs, (w, x, y))
    
    print(costs)

    nodes_set = UnionFind()
    total_cost = 0
    
    start_node = nodes[0][1]
    nodes_set.make_set(start_node)

    while costs:
        # Find the minimum cost edge
        cost, p1, p2 = heapq.heappop(costs)

        if p1 not in nodes_set or p2 not in nodes_set:
            total_cost += cost

            # Add the new node to the set
            if p1 not in nodes_set:
                nodes_set.make_set(p1)
            if p2 not in nodes_set:
                nodes_set.make_set(p2)

            # Union the sets
            nodes_set.union(p1, p2)
    
    for i in range(1, n + 1):
        nodes_set.make_set(i)

        if nodes_set.find(i) != nodes_set.find(nodes[0][1]):
            total_cost += nodes[i - 1][0] + nodes[0][0]

    print(total_cost)

if __name__ == "__main__":
    solve()
