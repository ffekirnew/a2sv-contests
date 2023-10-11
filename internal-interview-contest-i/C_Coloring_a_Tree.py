from collections import defaultdict


def solve():
    tree = defaultdict(list)
    parents = defaultdict(int)
    colors = defaultdict(int)
    tree_colors = defaultdict(int)

    n = int(input())
    edges = list(map(int, input().split()))
    colors_list = list(map(int, input().split()))

    for i, node in enumerate(edges):
        tree[node].append(i + 2)
        parents[i + 2] = node
    for i, color in enumerate(colors_list):
        colors[i + 1] = color

    root = 1
    operations = 0

    queue = [1]
    while queue:
        children = []

        for root in queue:
            if tree_colors[parents[root]] != colors[root]:
                operations += 1

            tree_colors[root] = colors[root]

            for child in tree[root]:
                children.append(child)
        queue = children

    print(operations)


if __name__ == "__main__":
    solve()
