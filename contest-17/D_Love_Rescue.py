import sys


class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

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
    n = int(input())
    source = sys.stdin.readline().strip()
    target = sys.stdin.readline().strip()

    union_find = DisjointSet()

    answer = []
    for i in range(n):
        union_find.make_set(source[i])
        union_find.make_set(target[i])

        if union_find.find(source[i]) != union_find.find(target[i]):

            union_find.union(source[i], target[i])
            answer.append([source[i], target[i]])
    
    print(len(answer))
    for line in answer:
        print(*line)
    

if __name__ == "__main__":
    solve()