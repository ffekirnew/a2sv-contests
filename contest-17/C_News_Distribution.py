import sys

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def __repr__(self) -> str:
        return f"{self.parent}"
    
    def get_size(self, x):
        return self.size[self.parent[self.find(x)]]

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
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.rank[root_x] += 1
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]


def solve():
    n, m = list(map(int, input().split()))
    friendships = DisjointSet(n + 1)

    for i in range(m):
        input_str = sys.stdin.readline().strip()

        if len(input_str) == 1:
            continue

        input_str = input_str.split()
        group = int(input_str[1])
        for i in range(2, len(input_str)):
            friendships.union(group, int(input_str[i]))

    for i in range(1, n + 1):
        print(friendships.get_size(i), end="")

        if i != n:
            print(" ", end="")


if __name__ == "__main__":
    solve()