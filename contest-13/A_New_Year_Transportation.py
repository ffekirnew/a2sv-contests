def solve():
    n, index = list(map(int, input().split()))
    portals = list(map(int, input().split()))

    graph = {}

    for i in range(1, n):
        graph[i] = i + portals[i - 1]

    curr_cell = 1
    while curr_cell <= index:
        if curr_cell == index:
            print("YES")
            return
        if curr_cell in graph:
            curr_cell = graph[curr_cell]

    print("NO")


if __name__ == "__main__":
    solve()
