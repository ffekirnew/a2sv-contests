from collections import defaultdict
import sys
import threading

def solve():
    num_chars, num_pairs = list(map(int, input().split()))
    golds_needed = list(map(int, input().split()))
    friendships = [list(map(int, input().split())) for _ in range(num_pairs)]

    friends = defaultdict(list)
    for p1, p2 in friendships:
        friends[p1].append(p2)
        friends[p2].append(p1)
    
    friendship_groups = []
    visited = set()
    def dfs(person):
        if person in visited:
            return

        visited.add(person)
        friendship_groups[-1].append(person)

        for friend in friends[person]:
            dfs(friend)

    for person in range(1, num_chars + 1):
        if person not in visited:
            friendship_groups.append([])
            dfs(person)

    answer = 0
    for group in friendship_groups:
        answer += min(golds_needed[friend - 1] for friend in group)

    print(answer)


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
solution_thread = threading.Thread(target = solve)
solution_thread.start()
solution_thread.join()