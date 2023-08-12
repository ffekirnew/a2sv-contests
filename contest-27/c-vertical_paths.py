import sys 

def solve():
    tests = int(input())
    for _ in range(tests):
        num_vertices = int(input())
        # the following list might be too long, use sys.stdin.readline() instead
        parents = list(map(int, sys.stdin.readline().split()))

        # build the tree and find the root
        tree = {}
        root = None
        non_leafs = set()
        for i in range(1, num_vertices + 1):
            if parents[i - 1] == i:
                root = i
            else:
                non_leafs.add(parents[i - 1])
                if parents[i - 1] not in tree:
                    tree[parents[i - 1]] = []
                tree[parents[i - 1]].append(i)

        # count all leafs
        print(num_vertices - len(non_leafs))

        # destroy parents list
        del parents

        # enumerate the paths
        stack = [(root, [root])]

        while stack:
            node, path = stack.pop()

            if node not in tree:
                print(len(path))
                print(*path)

            else:
                for i, child in enumerate(tree[node]):
                    if i == 0:
                        stack.append((child, path + [child]))
                    else:
                        stack.append((child, [child]))

        print()

if __name__ == "__main__":
    solve()
