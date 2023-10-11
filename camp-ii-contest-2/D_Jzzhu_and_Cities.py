from collections import defaultdict
from math import inf


def solve():
    n, m, k = list(map(int, input().split()))
    graph = defaultdict(list)

    for _ in range(m):
        from_, to_, length = list(map(int, input().split()))
        graph[from_].append((to_, length, 'R'))
    
    for _ in range(k):
        from_, to_, length = list(map(int, input().split()))
        graph[from_].append((to_, length, 'T'))
    
    distances = [inf] * n
    distances[0] = 0

    heap = [(0, 1, 0)]

        

if __name__ == "__main__":
    solve()